from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import *
from django.contrib.auth import get_user_model

from django.shortcuts import get_list_or_404, get_object_or_404

from .serializers import *
from .models import *
import random



# Create your views here.
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        random_movies = random.sample(movies, 20)
        random_serializer = movieListSerializer(random_movies[:20], many=True)

        likeMovies = get_object_or_404(get_user_model(), pk=request.user.pk)
        genre_score = {}
        for i in likeMovies.rated_movies.all():
            for j in i.genre_ids.all():
                genre_score[j.id] = genre_score.get(j.id, 0) + 1

        def usermovie_sort(movie):
            score = 0
            for i in movie.genre_ids.all():
                score += genre_score.get(i.id, 0)
            return score
        
        movies.sort(reverse=True, key=lambda x: (usermovie_sort(x), x.release_date))
        
        user_serializer = movieListSerializer(movies[:20], many=True)

        C = Movie.objects.aggregate(Sum('vote_average'))['vote_average__sum']/(len(movies))
        m = Movie.objects.order_by('vote_count')[int(0.9*len(movies))].vote_count
        
        def weight_rating(movie):
            v = movie.vote_count
            R = movie.vote_average
            return (v/(v+m) * R) + (m/(m+v) * C)
        
        movies.sort(key=lambda x: weight_rating(x), reverse=True)

        weight_serializer = movieListSerializer(movies[:20], many=True)
        
        data = {
            'random_data': random_serializer.data,
            'user_data': user_serializer.data,
            'weight_data': weight_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def random_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        movies = random.sample(movies, 20)
        serializer = movieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def all_movies(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = movieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def user_recommend_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        likeMovies = get_object_or_404(get_user_model(), pk=request.user.pk)
        
        genre_score = {}
        for i in likeMovies.rated_movies.all():
            for j in i.genre_ids.all():
                genre_score[j.id] = genre_score.get(j.id, 0) + 1
      

        def usermovie_sort(movie):
            score = 0
            for i in movie.genre_ids.all():
                score += genre_score.get(i.id, 0)
            return score 
        
        movies.sort(reverse=True, key=lambda x: (usermovie_sort(x), x.release_date))

        serializer = movieListSerializer(movies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def recommend_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)

        C = Movie.objects.aggregate(Sum('vote_average'))['vote_average__sum']/(len(movies))
        m = Movie.objects.order_by('vote_count')[int(0.9*len(movies))].vote_count
        
        def weight_rating(movie):
            v = movie.vote_count
            R = movie.vote_average
            return (v/(v+m) * R) + (m/(m+v) * C)

        movies.sort(key=lambda x: weight_rating(x), reverse=True)

        serializer = movieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        serializer = movieDetailSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET', 'POST'])
def comment(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        comments = movie.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'POST'])
def like_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        if movie.Like_users.filter(pk=request.user.pk).exists():
            movie.Like_users.remove(request.user)
        else:
            movie.Like_users.add(request.user)
        return Response(movieListSerializer(movie).data, status=status.HTTP_200_OK)
    
    elif request.method == 'GET':
        if movie.Like_users.filter(pk=request.user.pk).exists():
            is_like = True
        else:
            is_like = False

        data = {
            'state' : is_like
        }
        return Response(data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def job_movies(request, job, job_id):
    if request.method == 'GET':
        if job == 'cast':
            cast = get_object_or_404(Cast, pk=job_id)
            serializer = movieListSerializer(cast.movies.all(), many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        elif job == 'crew':
            crew = get_object_or_404(Crew, pk=job_id)
            serializer = movieListSerializer(crew.movies.all(), many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        
@api_view(['GET'])
def genre(request):
    print(request.GET['genre'])
    genres = request.GET['genre'] if request.GET.get('genre', False) else []
    print(genres)
    genres = list(genres.split(','))
    movies = Movie.objects.all()
    for i in genres:
        print(type(i))
        movies = movies.filter(genre_ids=int(i))

    movies = movies.order_by('-release_date')

    serializer = movieListSerializer(movies, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def comment_fix(request, comment_id):
    comment = get_object_or_404(CommentMovie, pk=comment_id)
    print(comment, request.data)
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        comment.delete()
        return Response('리뷰가 삭제되었습니다.', status=status.HTTP_204_NO_CONTENT)