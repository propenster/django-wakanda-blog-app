from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .models import Category
from .models import Comment
from .forms import CommentForm


class HomeView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blogapp/index.html' 
    context_object_name = 'blog_posts'
    ordering = ['-post_pub_date']
    paginate_by = 4


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blogapp/post_detail.html'

# def post_detail(request, pk):
#     template_name = 'blogapp/post_detail.html'
#     post = get_object_or_404(Post).comments.filter(active=True)
#     # comments = post.comments.filter(active=True)
#     new_comment = None
#     if(request.method == 'POST'):
#         comment_form = CommentForm(data=request.POST)
#         if(comment_form.is_valid()):
#             #create a comment object but dont save to db yet.
#             new_comment = comment_form.save(commit=False)
#             #Assign the cuttent post to the comment
#             new_comment.post = post
#             #save the comment to the database
#             new_comment.save()
#         else:
#             comment_form = CommentForm()
#     return render(request, template_name, {'post':post, 'new_comment':new_comment, 'comment_form':comment_form})


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blogapp/create_post.html'
    fields = ['post_title', 'post_category', 'post_body', 'post_image']
    

    def form_valid(self, form):
        form.instance.post_author = self.request.user
        return super().form_valid(form)


class CategoryListView(ListView):
    model = Category
    template_name = 'blogapp/base.html' 
    context_object_name = 'category_list'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blogapp/base.html' 
    