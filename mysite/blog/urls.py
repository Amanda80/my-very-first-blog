from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.posts_list,name='posts_list'),
]