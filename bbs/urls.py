from django.urls import re_path
from . import views


app_name = "bbs"
urlpatterns = [
    re_path(r'^$', views.index, name='bbs_index'),
    re_path(r'^detail/(\d+)/$', views.bbs_detail, name='bbs_detail'),
    re_path(r'^sub_comment/$', views.sub_comment, name='sub_comment'),
    re_path(r'^bbs_pub/$', views.bbs_pub, name='bbs_pub'),
    re_path(r'^bbs_sub/$', views.bbs_sub, name='bbs_sub'),
    re_path(r'^category/(\d+)/$', views.category, name='category'),
]
