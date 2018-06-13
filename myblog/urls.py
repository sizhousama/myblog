#!/user/bin/env python
# !-*-coding:utf-8 -*-
# !@Time     :2018/6/10 12:47
# !@Author   :sizhou
# !@File     :.py


from django.conf.urls import url
from . import views
app_name = 'myblog'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.ArticelDetailView.as_view(), name='detail'),
    url(r'^search/$', views.search, name='search'),
    url(r'^archives/$', views.archives, name='archives'),
]
