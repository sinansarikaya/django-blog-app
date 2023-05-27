from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list, name='index'),
    path('post-detail/<slug:slug>', post_detail, name='post_detail'),
    path('post-create/', post_create, name='add_post'),
    path('post-edit/<int:post_id>', post_edit, name='post_edit'),
]
