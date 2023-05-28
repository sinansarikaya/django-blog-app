from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list, name='index'),
    path('post-detail/<slug:slug>', post_detail, name='post_detail'),
    path('post-create/', post_create, name='add_post'),
    path('post-edit/<slug:slug>', post_edit, name='post_edit'),
    path('post-delete/<int:pk>', post_delete, name='post_delete'),
]
