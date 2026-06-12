import requests as http_requests

from django.conf import settings
from django.db import transaction
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from course.models import Course, Lesson, Module, UserCourse
from user.models import City, Profile, State, User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        token['name'] = getattr(user, 'profile', None) and user.profile.name or ''
        token['email'] = user.email
        return token


class UserSerializer(serializers.ModelSerializer):
    MIN_PASSWORD_LENGTH = 8

    role = serializers.ChoiceField(
        choices=['aluno', 'professor'],
        default='aluno',
        write_only=True,
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'validators': []},  # validate_email trata unicidade com mensagem em PT
        }

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError('E-mail já cadastrado.')
        return value

    def validate_password(self, value):
        if value is None or len(value) < self.MIN_PASSWORD_LENGTH:
            raise serializers.ValidationError(
                f'Senha deve ter pelo menos {self.MIN_PASSWORD_LENGTH} caracteres.'
            )
        return value

    @transaction.atomic
    def create(self, validated_data):
        role = validated_data.pop('role', 'aluno')
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        user.is_teacher = (role == 'professor')
        user.is_student = (role == 'aluno')
        user.save()
        Profile.objects.create(user=user)
        return user


class PasswordChangeSerializer(serializers.Serializer):
    MIN_PASSWORD_LENGTH = 8
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Senha atual inválida.')
        return value

    def validate_new_password(self, value):
        if value is None or len(value) < self.MIN_PASSWORD_LENGTH:
            raise serializers.ValidationError(
                f'Senha deve ter pelo menos {self.MIN_PASSWORD_LENGTH} caracteres.'
            )
        return value

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name', 'abbreviation']


class CitySerializer(serializers.ModelSerializer):
    state = serializers.SlugRelatedField(read_only=True, slug_field='abbreviation')

    class Meta:
        model = City
        fields = ['id', 'name', 'state']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video_url', 'order']


class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, required=False)

    class Meta:
        model = Module
        fields = ['id', 'title', 'order', 'lessons']

    def create(self, validated_data):
        lessons_data = validated_data.pop('lessons', [])
        module = Module.objects.create(**validated_data)
        for lesson_data in lessons_data:
            Lesson.objects.create(module=module, **lesson_data)
        return module

    def update(self, instance, validated_data):
        lessons_data = validated_data.pop('lessons', [])
        instance.title = validated_data.get('title', instance.title)
        instance.order = validated_data.get('order', instance.order)
        instance.save()

        existing_lessons = {str(les.id): les for les in instance.lessons.all()}
        incoming_ids = set()

        for lesson_data in lessons_data:
            lesson_id = lesson_data.get('id')
            if lesson_id and str(lesson_id) in existing_lessons:
                lesson = existing_lessons[str(lesson_id)]
                lesson.title = lesson_data.get('title', lesson.title)
                lesson.video_url = lesson_data.get('video_url', lesson.video_url)
                lesson.order = lesson_data.get('order', lesson.order)
                lesson.save()
                incoming_ids.add(str(lesson_id))
            else:
                Lesson.objects.create(module=instance, **lesson_data)

        for lid, lesson in existing_lessons.items():
            if lid not in incoming_ids:
                lesson.delete()

        return instance


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.SlugRelatedField(slug_field='email', read_only=True)
    modules_count = serializers.SerializerMethodField()
    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'duration', 'level',
            'emoji', 'thumb_bg', 'teacher', 'is_published', 'status',
            'modules_count', 'lessons_count',
        ]
        read_only_fields = ['id', 'teacher', 'is_published', 'status']

    def get_modules_count(self, obj):
        return obj.modules.count()

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(module__course=obj).count()


class TeacherDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    def get_name(self, obj):
        return getattr(getattr(obj, 'profile', None), 'name', '') or ''

    def get_photo(self, obj):
        profile = getattr(obj, 'profile', None)
        if not profile or not profile.photo:
            return None
        request = self.context.get('request')
        return request.build_absolute_uri(profile.photo.url) if request else profile.photo.url

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'photo']


class CourseDetailSerializer(serializers.ModelSerializer):
    teacher = TeacherDetailSerializer(read_only=True)
    modules = ModuleSerializer(many=True, required=False)

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'duration', 'level',
            'emoji', 'thumb_bg', 'teacher', 'is_published', 'status', 'modules',
        ]
        read_only_fields = ['id', 'teacher', 'is_published', 'status']

    def create(self, validated_data):
        modules_data = validated_data.pop('modules', [])
        course = Course.objects.create(**validated_data)
        for module_data in modules_data:
            lessons_data = module_data.pop('lessons', [])
            module = Module.objects.create(course=course, **module_data)
            for lesson_data in lessons_data:
                Lesson.objects.create(module=module, **lesson_data)
        return course

    def update(self, instance, validated_data):
        modules_data = validated_data.pop('modules', [])

        for attr in [
            'title', 'description', 'duration', 'level', 'emoji', 'thumb_bg',
        ]:
            if attr in validated_data:
                setattr(instance, attr, validated_data[attr])
        instance.save()

        existing_modules = {str(m.id): m for m in instance.modules.all()}
        incoming_ids = set()

        for module_data in modules_data:
            module_id = module_data.get('id')
            if module_id and str(module_id) in existing_modules:
                module = existing_modules[str(module_id)]
                module.title = module_data.get('title', module.title)
                module.order = module_data.get('order', module.order)
                module.save()

                # Sync lessons inside this module
                lessons_data = module_data.get('lessons', [])
                existing_lessons = {str(les.id): les for les in module.lessons.all()}
                lesson_incoming_ids = set()
                for lesson_data in lessons_data:
                    lesson_id = lesson_data.get('id')
                    if lesson_id and str(lesson_id) in existing_lessons:
                        lesson = existing_lessons[str(lesson_id)]
                        lesson.title = lesson_data.get('title', lesson.title)
                        lesson.video_url = lesson_data.get('video_url', lesson.video_url)
                        lesson.order = lesson_data.get('order', lesson.order)
                        lesson.save()
                        lesson_incoming_ids.add(str(lesson_id))
                    else:
                        Lesson.objects.create(module=module, **lesson_data)
                for lid, lesson in existing_lessons.items():
                    if lid not in lesson_incoming_ids:
                        lesson.delete()

                incoming_ids.add(str(module_id))
            else:
                lessons_data = module_data.pop('lessons', [])
                module = Module.objects.create(course=instance, **module_data)
                for lesson_data in lessons_data:
                    Lesson.objects.create(module=module, **lesson_data)

        for mid, module in existing_modules.items():
            if mid not in incoming_ids:
                module.delete()

        return instance


class PublishedCourseSerializer(serializers.ModelSerializer):
    teacher = TeacherDetailSerializer(read_only=True)
    modules_count = serializers.SerializerMethodField()
    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'duration', 'level',
            'emoji', 'thumb_bg', 'teacher', 'is_published', 'status',
            'modules_count', 'lessons_count',
        ]
        read_only_fields = ['id', 'is_published', 'status']

    def get_modules_count(self, obj):
        return obj.modules.count()

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(module__course=obj).count()


class AdminCourseSerializer(serializers.ModelSerializer):
    teacher = TeacherDetailSerializer(read_only=True)
    modules_count = serializers.SerializerMethodField()
    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'duration', 'level',
            'emoji', 'thumb_bg', 'teacher', 'status', 'is_published',
            'modules_count', 'lessons_count',
        ]
        read_only_fields = ['id', 'title', 'teacher', 'is_published']

    def get_modules_count(self, obj):
        return obj.modules.count()

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(module__course=obj).count()


class TeacherStudentSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    student_email = serializers.SerializerMethodField()
    student_photo = serializers.SerializerMethodField()
    course_id = serializers.UUIDField(source='course.id', read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)

    def get_student_name(self, obj):
        return obj.profile.name or ''

    def get_student_email(self, obj):
        return obj.profile.user.email

    def get_student_photo(self, obj):
        if not obj.profile.photo:
            return None
        request = self.context.get('request')
        return request.build_absolute_uri(obj.profile.photo.url) if request else obj.profile.photo.url

    class Meta:
        model = UserCourse
        fields = [
            'id', 'student_name', 'student_email', 'student_photo',
            'course_id', 'course_title', 'started_at', 'is_completed',
        ]


class AdminUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    role = serializers.SerializerMethodField()
    city_detail = CitySerializer(source='city', read_only=True)

    def get_role(self, obj):
        return obj.user.role

    class Meta:
        model = Profile
        fields = ['email', 'name', 'photo', 'role', 'city_detail']


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    city_detail = CitySerializer(source='city', read_only=True)
    role = serializers.ChoiceField(
        choices=['aluno', 'professor'],
        write_only=True,
        required=False,
    )

    class Meta:
        model = Profile
        fields = ['email', 'name', 'photo', 'celular', 'telephone', 'birthday', 'city', 'city_detail', 'role']
        extra_kwargs = {
            'city': {'required': False, 'allow_null': True},
            'photo': {'required': False, 'allow_null': True},
            'celular': {'required': False, 'allow_blank': True, 'allow_null': True},
            'telephone': {'required': False, 'allow_blank': True, 'allow_null': True},
            'birthday': {'required': False, 'allow_null': True},
            'name': {'required': False},
        }

    def update(self, instance, validated_data):
        role = validated_data.pop('role', None)
        if role is not None:
            instance.user.is_teacher = (role == 'professor')
            instance.user.is_student = (role == 'aluno')
            instance.user.save()
        return super().update(instance, validated_data)


GOOGLE_TOKENINFO_URL = 'https://oauth2.googleapis.com/tokeninfo'


class GoogleSocialAuthSerializer(serializers.Serializer):
    credential = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(
        choices=['aluno', 'professor'],
        default='aluno',
        required=False,
    )

    def validate_credential(self, value):
        try:
            resp = http_requests.get(
                GOOGLE_TOKENINFO_URL,
                params={'id_token': value},
                timeout=5,
            )
        except http_requests.RequestException:
            raise serializers.ValidationError(
                'Não foi possível verificar o token com o Google.'
            )

        if resp.status_code != 200:
            raise serializers.ValidationError(
                'Token do Google inválido ou expirado.'
            )

        id_info = resp.json()

        if id_info.get('aud') != settings.GOOGLE_CLIENT_ID:
            raise serializers.ValidationError(
                'Token não autorizado para esta aplicação.'
            )

        if id_info.get('email_verified') != 'true':
            raise serializers.ValidationError(
                'E-mail da conta Google não verificado.'
            )

        if not id_info.get('email'):
            raise serializers.ValidationError(
                'Não foi possível obter o e-mail da conta Google.'
            )

        return id_info



