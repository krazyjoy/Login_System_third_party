from rest_framework import serializers
from .models import TestUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestUser
        fields = ['name', 'email', 'password', 'register_from', 'avatar', 'gender', 'birthday', 'phone', 'website', 'biography', 'state', 'city', 'address', 'country', 'zipcode']
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        user = TestUser(
            name = validated_data['name'],
            email = validated_data['email'],
            register_from = validated_data['register_from'],
            avatar = validated_data['avatar'],
            gender = validated_data['gender'],
            birthday = validated_data['birthday'],
            phone = validated_data['phone'],
            website = validated_data['website'],
            biography = validated_data['biography'],
            zipcode = validated_data['zipcode'],
            country = validated_data['country'],
            state = validated_data['state'],
            city = validated_data['city'],
            address = validated_data['address'],

        )

        user.set_password(validated_data['password'])
        user.save()
        return user