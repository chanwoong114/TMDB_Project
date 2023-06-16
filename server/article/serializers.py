from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ['id', 'username','profile']

    like_counts = serializers.IntegerField(source='like_users.count', read_only=True)
    user = UserSerializer(read_only=True)
    comment_counts = serializers.IntegerField(source='comments.count', read_only=True)


    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'user', 'updated_at', 'like_counts', 'comment_counts']


class CommentSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ['id', 'username']

    user = UserSerializer(read_only=True)
    like_counts = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['like_users', 'article']


class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ['id', 'username']

    comments = CommentSerializer(many=True, read_only=True)
    comment_counts = serializers.IntegerField(source='comments.count', read_only=True)
    user = UserSerializer(read_only=True)
    like_counts = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['like_users']