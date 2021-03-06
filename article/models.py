from django.db import models
from django.contrib.auth.models import User

class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    is_deleted = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    # def __str__(self):
    #     return "<Article: %s>" % self.title