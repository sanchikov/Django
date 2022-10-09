from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', index, name='index'),
    path('new/<str:slug>', detail, name='detail'),
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),



]
