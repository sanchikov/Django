"""
    Здесь зарегистрированы модели для приложения 'blog'
"""

from django.contrib import admin
from .models import Post, PostCategory, Author

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostCategory)
