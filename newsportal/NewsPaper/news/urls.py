from django.urls import path
# Импортируем созданное нами представление
from .views import PostList
from django import index

urlpatterns = [
    path('news_list/', index),
]
