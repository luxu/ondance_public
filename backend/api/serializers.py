from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'email',
            'address',
            'ein',
            'cellphone',
            'phone',
            'password',
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
