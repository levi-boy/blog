from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Blog
from .forms import BlogCreateForm

class BlogListView(ListView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_blog'] = Blog.objects.latest('created')
        return context


    last_blog = Blog.objects.latest('created')
    queryset = Blog.objects.exclude(id=last_blog.id)
    context_object_name = 'blogs'
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/blog_detail.html'


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog/blog_create.html'
    form_class = BlogCreateForm
    


