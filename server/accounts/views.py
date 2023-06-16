from django.shortcuts import render, get_list_or_404, get_object_or_404
from .serializers import *
from movies.models import *
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def mypage(request):
    user = get_object_or_404(get_user_model(), pk=request.user.pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return Response('회원 탈퇴 되었습니다.')
    

@api_view(['POST'])
def follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    if person == request.user:
        return Response('본인은 본인을 팔로우 할 수 없습니다.', status=status.HTTP_400_BAD_REQUEST)
    
    if person.followers.filter(pk=request.user.pk).exists():
        person.followers.remove(request.user)
        return Response({'id': user_pk, 'follow': False})
    else:
        person.followers.add(request.user)
        return Response({'id': user_pk, 'follow': True})
    
@api_view(['GET', 'POST'])
def userpage(request, username):
    if request.method == 'GET':
        person = get_object_or_404(get_user_model(), username=username)
        serializer = UserSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def profile_change(request, profile_num):
    person = get_object_or_404(get_user_model(), pk=request.user.pk)
    if request.method == 'PUT':
        person.profile = f'accounts/{profile_num}.png'
        person.save()
        return Response('프로필 변경 완료', status=status.HTTP_200_OK)