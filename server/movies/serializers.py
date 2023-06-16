from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class CommentSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ['id', 'username']

    user = UserSerializer(read_only=True)

    class Meta:
        model = CommentMovie
        fields = '__all__'
        read_only_fields = ['user', 'movie']

class movieListSerializer(serializers.ModelSerializer):

    comments_rating = serializers.SerializerMethodField('get_comments_rating')

    class Meta:
        model = Movie
        fields = '__all__'

    def get_comments_rating(self, obj):
        comments = CommentMovie.objects.filter(movie=obj)
        Sum = 0
        if len(comments) > 0:
            for comment in comments:
                Sum += comment.rating
        
            Sum /= len(comments)

        return Sum

class movieDetailSerializer(serializers.ModelSerializer):

    class genreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'

    class castSerializer(serializers.ModelSerializer):
        class Meta:
            model = Cast
            fields = ['id', 'name', 'profile_path', 'character']

    class crewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Crew
            fields = '__all__'
    
    genre_ids = genreSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)
    comments_rating = serializers.SerializerMethodField('get_comments_rating')
    crew_ids = crewSerializer(read_only=True)
    cast_ids = castSerializer(many=True, read_only=True)
    recommends = serializers.IntegerField(source='recommends.count', read_only=True)
    recommend_movies = movieListSerializer(many=True, read_only=True)
    Like_users_count = serializers.IntegerField(source='Like_users.count', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


    def get_comments_rating(self, obj):
        comments = CommentMovie.objects.filter(movie=obj)
        Sum = 0
        if len(comments) > 0:
            for comment in comments:
                Sum += comment.rating
        
            Sum /= len(comments)

        return Sum