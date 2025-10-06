from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'categories']
        widgets = {
            'categories': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']