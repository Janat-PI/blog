from django.views.generic import ListView, DetailView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from main.models import Category, Post
from django.views import View
from django.shortcuts import render

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

class IndexPageView(View):
    def get(self, request):
        catagories = Category.objects.all()
        posts = Post.objects.all()
        return render(request, 'main/index.html', locals())


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


class CreateNewPostView(LoginRequiredMixin, CreateView):
    queryset = Post.objects.all()
    template_name = 'main/create_post.html'
    form_class = CreatePostForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        return reverse('post-details', args=(self.object.id,))


class IsAuthorMixin(UserPassesTestMixin):
    def test_func(self):
        post = self.get_object()
        return self.request.user.is_authenticated and \
            self.request.user == post.author


class EditPostView(IsAuthorMixin, UpdateView):
    queryset = Post.objects.all()
    template_name = 'main/edit_post.html'
    form_class = UpdatePostView

    def get_success_url(self):
        return reverse('post-details', args=(self.object.id, ))


class DeletePostView(IsAuthorMixin, DetailView):
    queryset = Post.objects.all()
    template_name = 'main/delete_post.html'

    def get_success_url(self):
        return reverse('index-page')

class SearchResultView(View):
    pass


#TODO: Создание, редактирование и удаление постоов
#TODO: Фильтрация, поиск, сортирова
#TODO: Пагинация
#TODO: Переипользование шаблонов
#TODO: Проверка прав
#TODO: Избранное
#TODO: Дизайн
#TODO: html - message


