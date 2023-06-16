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
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        articles.sort(key=lambda x: x.updated_at,reverse=True)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=article)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'DELETE':
        article.delete()
        return Response('게시글이 삭제되었습니다.', status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response('댓글이 삭제되었습니다.', status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def like_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if article.user == request.user:
        return Response('본인은 본인글에 좋아요를 누를 수 없습니다.')
    if request.method == 'POST':
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            return Response('좋아요 취소')
        else:
            article.like_users.add(request.user)
            return Response('좋아요')
        

@api_view(['POST'])
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.user == request.user:
        return Response('본인은 본인 댓글에 좋아요를 누를 수 없습니다.')
    if request.method == 'POST':
        if comment.like_users.filter(pk=request.user.pk).exists():
            comment.like_users.remove(request.user)
            return Response('좋아요 취소')
        else:
            comment.like_users.add(request.user)
            return Response('좋아요')