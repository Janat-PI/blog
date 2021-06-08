from django.views.generic import ListView, DetailView

from main.models import Category, Post


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





#TODO: Регистрация, активация, логин, логаут
#TODO: Фильтрация, поиск, сортирова
#TODO: Пагинация
#TODO: Переипользование шаблонов
#TODO: Проверка прав
#TODO: Избранное
#TODO: Дизайн
#TODO: html - message


