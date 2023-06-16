from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('<int:article_id>/', views.article_detail),
    path('comments/<int:comment_id>/', views.comment_detail),
    path('comments/', views.comment_list),
    path('<int:article_id>/like/', views.like_article),
    path('comments/<int:comment_id>/like/', views.like_comment),
]
