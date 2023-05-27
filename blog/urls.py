from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list, name='index'),
    path('post-detail/<int:post_id>', post_detail, name='post_detail'),
    path('post-create/', post_create, name='add_blog'),
    path('post-edit/<int:post_id>', post_edit, name='post_edit'),
]
