from django.urls import path
from .views import show_all_post, add_post

urlpatterns = [
    path('all-posts/', show_all_post),
    path('add-post/', add_post),
]