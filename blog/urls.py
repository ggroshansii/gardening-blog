from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index),
    path('posts/', views.posts),
    path('posts/<post_detail>/', views.post_detail)
]