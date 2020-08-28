from django import forms

from .models import Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'browser-default blog-create__title', 'placeholder': 'Введите название статьи'}),
            'text': CKEditorUploadingWidget(),
            'file': forms.FileInput(attrs={'class': 'blog-create__image'})
        }


