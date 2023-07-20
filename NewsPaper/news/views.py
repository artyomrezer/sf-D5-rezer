from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.views import View
from .models import Post
from datetime import datetime
from django.core.paginator import Paginator
from .filters import NewsFilter
from .forms import NewsForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

class NewsList(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    queryset = Post.objects.order_by('-id')
    ordering = ['-id']
    paginate_by = 10
    form_class = NewsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['choices'] = Post.CATEGORY_CHOICES
        context['form'] = NewsForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)
    
class NewsSearch(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'news_search_result'
    ordering = ['-id']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'show_post.html'
    context_object_name = 'show_post'

class News(View):
    
    def get(self, request):
        news = Post.objects.order_by('-id')
        p = Paginator(news, 1)
        news = p.get_page(request.GET.get('page', 1))
        data = {
        'news_list': news,
        }
        return render(request, 'news_list.html', data)
    
class PostDetailView(DetailView):
   model = Post
   template_name = 'post_detail.html'
   context_object_name = 'one_post'

class PostCreateView(PermissionRequiredMixin, CreateView):
   model = Post
   template_name = 'post_create.html'
   form_class = NewsForm
   permission_required = ('news.add_post', )
 
class ProductUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
   model = Post
   template_name = 'post_create.html'
   form_class = NewsForm
#    redirect_field_name = None
   permission_required = ('news.change_post', )

   def get_object(self, **kwargs):
       id = self.kwargs.get('pk')
       return Post.objects.get(pk=id)

class ProductDeleteView(DeleteView):
   template_name = 'product_delete.html'
   context_object_name = 'one_post'
   queryset = Post.objects.all()
   success_url = reverse_lazy('news:news_list')



