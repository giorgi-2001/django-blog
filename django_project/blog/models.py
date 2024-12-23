from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField(max_length=100, null=False)
    body = models.TextField(null=False)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"slug": self.slug})
    
