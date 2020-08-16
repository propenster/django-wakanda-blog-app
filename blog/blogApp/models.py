from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    post_title = models.CharField(max_length=150)
    post_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    post_body = models.TextField()
    post_image = models.FileField(upload_to='media/images/', help_text='Set feature image', default='settings.MEDIA_ROOT/images/image_3.jpg')
    post_pub_date = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_author = models.CharField(max_length=80)
    comment_author_email = models.EmailField()
    comment_body = models.TextField()
    comment_pub_date = models.DateTimeField(auto_now_add=True)
    comment_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-comment_pub_date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment_body, self.comment_author)    
