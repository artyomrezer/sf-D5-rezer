from django.urls import path
from .views import NewsList, NewsSearch, PostDetail, News, PostDetailView, PostCreateView, ProductUpdateView, ProductDeleteView

app_name = 'news'
urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('search/', NewsSearch.as_view()),
    path('<int:pk>/single_news', PostDetail.as_view()),
    path('news_pages/', News.as_view()),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit', ProductUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='post_delete'),
]