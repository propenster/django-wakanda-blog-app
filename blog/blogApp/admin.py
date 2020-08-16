from django.contrib import admin
from .models import Category
from .models import Post
from .models import Comment

admin.site.register(Category)
admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_author', 'comment_body', 'comment_post', 'comment_pub_date', 'comment_active')

    list_filter = ('comment_active', 'comment_pub_date')

    search_fields = ('comment_author', 'comment_author_email', 'comment_body')

    actions = ['approve_comments']


    def approve_comments(self, request, queryset):
        queryset.update(comment_active=True)
