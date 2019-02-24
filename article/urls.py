from django.urls import re_path
from . import views


app_name = "article"
urlpatterns = [
    re_path(r'^article-column/$', views.article_column, name="article_column"),
]