from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .models import Category


class HomeView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blogapp/index.html'
    context_object_name = 'blog_posts'
    ordering = ['-post_pub_date']
    paginate_by = 4


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blogapp/post_detail.html'


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blogapp/create_post.html'
    fields = ['post_title', 'post_category', 'post_body']

    def form_valid(self, form):
        form.instance.post_author = self.request.user
        return super().form_valid(form)
