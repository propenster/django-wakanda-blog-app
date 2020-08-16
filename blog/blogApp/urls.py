from django.urls import include, path
from .views import HomeView, PostDetailView, CreatePostView


urlpatterns = [
    path('posts/', HomeView.as_view(), name='blog-home'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('posts/create-post', CreatePostView.as_view(success_url='/posts'), name='create-post')
]
