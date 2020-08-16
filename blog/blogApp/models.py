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
    # post_image = models.ImageField(upload_to=get_upload_path, help_text='Image to process')
    post_pub_date = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title
    
