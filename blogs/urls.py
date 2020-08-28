from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.BlogCreateView.as_view(), name="blog_create"),
    path('detail_<int:pk>/', views.BlogDetailView.as_view(), name="blog_detail"),
    path('', views.BlogListView.as_view(), name="blog_list"),
]