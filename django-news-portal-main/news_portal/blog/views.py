from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


class PostsList(ListView):
    """ Представление всех постов в виде списка. """
    paginate_by = 4
    model = Post
    ordering = 'date_time'
    template_name = 'posts.html'
    context_object_name = 'posts'


class SearchPosts(ListView):
    """ Представление всех постов в виде списка. """
    paginate_by = 3
    model = Post
    ordering = 'date_time'
    template_name = 'search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """ Переопределяем функцию получения списка статей. """
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs) -> dict:
        """ Метод get_context_data позволяет изменить набор данных, который будет передан в шаблон. """
        context = super().get_context_data(**kwargs)
        context['search_filter'] = self.filterset
        return context


class PostDetail(DetailView):
    """ Представление отдельного поста. """
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class ArticleCreate(PermissionRequiredMixin, CreateView):
    """ Представление для создания статьи. """
    permission_required = ('blog.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Добавить статью"
        return context


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    """ Представление для редактирования статьи. """
    permission_required = ('blog.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Редактировать статью"
        return context


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    """ Представление для удаления статьи. """
    permission_required = ('blog.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Удалить статью"
        context['previous_page_url'] = reverse_lazy('posts_list')
        return context


class NewsCreate(PermissionRequiredMixin, CreateView):
    """ Представление для создания новости. """
    permission_required = ('blog.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Добавить новость"
        return context


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    """ Представление для редактирования новости. """
    permission_required = ('blog.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Редактировать новость"
        return context


class NewsDelete(PermissionRequiredMixin, DeleteView):
    """ Представление для удаления новости. """
    permission_required = ('blog.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Удалить новость"
        context['previous_page_url'] = reverse_lazy('posts_list')
        return context


@login_required
def add_subscribe(request, pk):
    Category.objects.get(pk=pk).subscribers.add(request.user)
    return redirect('/news/')

@login_required
def del_subscribe(request, pk):
    Category.objects.get(pk=pk).subscribers.remove(request.user)
    return redirect('/news/')