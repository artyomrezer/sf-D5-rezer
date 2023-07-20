from django_filters import FilterSet
from .models import Post
 
class NewsFilter(FilterSet):
    class Meta:
        model = Post
        # fields = ('dateCreation', 'title', 'author')
        fields = {
        'dateCreation': ['gt'],
        'title': ['icontains'], # Ищем по ключевым словам в описании
        'author' : ['exact'] # Поле для работы с choices
        }