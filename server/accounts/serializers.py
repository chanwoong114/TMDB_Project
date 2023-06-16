from rest_framework import serializers
from movies.models import *
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class FollowingSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ['id', 'username']

    class MovieSerializer(serializers.ModelSerializer):
        comments_rating = serializers.SerializerMethodField('get_comments_rating')

        class Meta:
            model = Movie
            fields = ['id', 'title', 'poster_path', 'comments_rating']

        def get_comments_rating(self, obj):
            comments = CommentMovie.objects.filter(movie=obj)
            Sum = 0
            if len(comments) > 0:
                for comment in comments:
                    Sum += comment.rating
            
                Sum /= len(comments)

            return Sum

    rated_movies = MovieSerializer(many=True, read_only=True)
    followings = FollowingSerializer(many=True, read_only=True)
    follower_count = serializers.IntegerField(source='followers.count', read_only=True)
    followings_count = serializers.IntegerField(source='followings.count', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'rated_movies', 'profile', 'followers', 'followings', 'follower_count', 'followings_count']

    