from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_id>/', views.movie_detail),
    path('random/', views.random_list),
    path('recommend_list/', views.recommend_list),
    path('<int:movie_id>/comments/', views.comment),
    path('comment/comment_fix/<int:comment_id>/', views.comment_fix),
    path('<int:movie_id>/like/', views.like_movie),
    path('<str:job>/<int:job_id>/', views.job_movies),
    path('user_recommend_list/', views.user_recommend_list),
    path('genre/', views.genre),
    path('all/', views.all_movies),
]
