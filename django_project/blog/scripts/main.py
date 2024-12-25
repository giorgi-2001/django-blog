import json
import random
from pathlib import Path
from django.contrib.auth.models import User
from blog.models import Post

FILE_PATH = Path(__file__).parent / "posts.json"

def main():
    users = list(User.objects.all())

    with open(FILE_PATH) as f:
        posts = json.load(f)
        for post in posts:
            Post.objects.create(**post, author=random.choice(users))

