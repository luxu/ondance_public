from rest_framework import serializers

from course.models import Course
from user.models import City, State, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name'],
            ein=validated_data['ein']
        )
        user.set_password(validated_data['password'])
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


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.SlugRelatedField(
        slug_field='email',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Course
        fields = ['id', 'title', 'teacher', 'is_published', 'status']
        read_only_fields = ['id', 'is_published', 'status']


# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = (
#             'id',
#             'first_name',
#             "last_name",
#             "email",
#             "national_registration",
#             "cellphone",
#             "phone",
#             "active"
#         )
