from rest_framework import serializers
from .models import TestUser
from articles.serializer import ArticleSerializer

class UserSerializer(serializers.ModelSerializer):
    blocked_articles = ArticleSerializer(many=True, read_only=True, source='get_blocked_articles')

    class Meta:
        model = TestUser

        fields = ['name', 'email', 'password', 'register_from', 'avatar',
                  'gender', 'birthday', 'phone', 'website', 'biography',
                  'state', 'city', 'address', 'country', 'zipcode',
                  'block', 'blocked_articles']
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        user = TestUser(
            name = validated_data['name'],
            email = validated_data['email'],

        )

        user.set_password(validated_data['password'])
        user.save()
        return user
