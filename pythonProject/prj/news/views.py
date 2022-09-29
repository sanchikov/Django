from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Post, PostCategory
from .filters import PostFilter
from .forms import NewPostForm

class PostList(ListView):
   model = Post
   template_name = 'index.html'
   context_object_name = 'post'
   paginate_by = 2
   form_class = NewPostForm


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
    # context['categories'] = PostCategory.objects.all()
    # context['form'] = NewPostForm()
    # return context


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