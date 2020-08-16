from django.urls import include, path
from .views import HomeView, PostDetailView, CreatePostView, CategoryListView, CategoryDetailView


urlpatterns = [
    path('posts/', HomeView.as_view(), name='blog-home'),
    # path('posts/<int:pk>', post_detail, name='post-detail'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('posts/create-post', CreatePostView.as_view(success_url='/posts'), name='create-post'),
    path('posts/categories', CategoryListView.as_view(), name='categories'),
    path('posts/categories/<int:pk>', CategoryDetailView.as_view(), name='category'),
]
