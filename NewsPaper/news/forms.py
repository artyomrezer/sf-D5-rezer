from django.forms import ModelForm
from .models import Post
from django import forms
 
class NewsForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'categoryType', 'text']
        widgets = {
         'author' : forms.Select(attrs={
           'class': 'form-control',
           'placeholder': 'Введите автора'
         }),
         'title' : forms.TextInput(attrs={
           'class': 'form-control',
           'placeholder': 'Введите заголовок'
         }),
         'categoryType' : forms.Select(attrs={
           'class': 'form-control',
         }),
         'text' : forms.Textarea(attrs={
           'class': 'form-control',
         }),
       }