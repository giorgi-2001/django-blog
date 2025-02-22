from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="avatars")

    def __str__(self):
        return f"{self.user.username}'s Profile"
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.width > 300 or img.height > 300:
            size = (300, 300)
            img.thumbnail(size)
            img.save(self.image.path)
