from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import *
from .models import *
from .filters import Postfilter
from .forms import *
from datetime import *
from django.views import View
from django.core.paginator import Paginator

class NewsList(ListView):
   model = Post
   template_name = 'news.html'
   context_object_name = 'news_list'
   paginate_by = 6
   ordering = ['-dateCreation']
   form_class = NewPostForm


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['category_it'] = Category.objects.get(category_name='IT').id
    context['category_live'] = Category.objects.get(category_name='Live').id
    context['category_auto'] = Category.objects.get(category_name='Auto').id
    context['category_weather'] = Category.objects.get(category_name='Weather').id
    context['category_money'] = Category.objects.get(category_name='Money').id
    context['current_time'] = datetime.now()
    return context

@staticmethod
def post(self, request):
    request.session['django_timezone'] = request.POST['timezone']
    return redirect('/profile')

def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
    if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
        form.save()
    return super().get(request, *args, **kwargs)


class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'post'
    queryset = Post.objects.order_by('dateCreation')
    paginate_by = 1

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


def index(request):
    news = Post.objects.all()
    return render(request, 'index.html', context={'news': news})

def detail(request, slug):
    news = Post.objects.get(slug__iexact=slug)
    return render(request, 'details.html', context={'Post': Post})


class NEWSOne(DetailView):
   model = Post
   template_name = 'post.html'
   context_object_name = 'post'


   def get_queryset(self):
       # Получаем обычный запрос
       queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       self.filterset = PostFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список товаров
       return self.filterset.qs

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context

class PostCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = NewPostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'product_edit.html'

class PostUpdate(UpdateView):
    form_class = NewPostForm
    model = Post
    template_name = 'post_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('product_list')