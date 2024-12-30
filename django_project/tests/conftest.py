import pytest
import tempfile
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image

import os

from blog.models import Post, User


@pytest.fixture
def user():
    return User.objects.create(
        username="TestUser",
        password="newpassword123"
    )


@pytest.fixture
def post_factory(user):
    def create(
        title="Django Post",
        body="This is a django post",
        slug="django-post",
        author=user
    ):
        post = Post.objects.create(
            title=title,
            body=body,
            slug=slug,
            author=author
        )
        post.full_clean()
        return post
    
    return create


@pytest.fixture
def large_image():
    image = Image.new("RGB", (500, 500), "green")

    temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    image.save(temp_file, "PNG")

    temp_file.close()

    return SimpleUploadedFile(
        "test_img.png",
        open(temp_file.name, "rb").read(),
        content_type="image/png"
    )


@pytest.fixture
def profile_with_img(user, large_image):
    user.profile.image = large_image
    user.profile.save()

    yield user.profile
    
    if os.path.exists(user.profile.image.path):
        os.remove(user.profile.image.path)

