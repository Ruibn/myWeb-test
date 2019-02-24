from django.urls import re_path
from . import views


app_name = 'blog'
urlpatterns = [
    re_path(r'^$', views.blog_title, name="blog_title"),
    re_path(r'(?P<article_id>\d)/$', views.blog_article, name="blog_detail"),
]
