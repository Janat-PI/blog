from django.views.generic import ListView, DetailView, CreateView, UpdateView, DetailView

from main.models import Category, Post

from .forms import *


# def index_page(request):
#     categories = Category.objects.all()
#     return render(request,
#                   'main/index.html',
#                   {'categories': categories})


# class IndexPageView(View):
#
#     def get(self, request):
#         categories = Category.objects.all()
#         return  render(request,
#                         'main/index.html',
#                         {'categories': categories})

class IndexPageView(ListView):
    queryset = Category.objects.all()
    template_name = 'main/index.html'
    context_object_name = 'categories'


class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'main/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category')
        return queryset.filter(category_id=category_id)


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'main/post_details.html'


class CreateNewPostView(CreateView):
    queryset = Post.objects.all()
    template_name = 'main/create_post.html'
    form_class = CreatePostForm


class EditPostView(UpdateView):
    queryset = Post.objects.all()
    template_name = 'main/edit_post.html'
    form_class = UpdatePostView


class DeletePostView(DetailView):
    queryset = Post.objects.all()
    template_name = 'main/delete_post.html'



#TODO: Создание, редактирование и удаление постоов
#TODO: Фильтрация, поиск, сортирова
#TODO: Пагинация
#TODO: Переипользование шаблонов
#TODO: Проверка прав
#TODO: Избранное
#TODO: Дизайн
#TODO: html - message


