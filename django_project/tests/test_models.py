import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.urls import reverse
from PIL import Image

import os



@pytest.mark.parametrize(
    "title, body, slug, valid",
    [
        ("bla bla", "bla bla bla", "bla-bla", True),
        ("", "bla bla bla", "bla-bla", False),
        ("bla bla", "", "bla-bla", False),
        ("bla bla", "bla bla bla", "", False),
        ("bla bla", "bla bla bla", "Invalid Slug", False),
        ("bla bla", "bla bla bla", "Iinvalid-slug-$", False),
    ]
)
def test_post_valid(db, post_factory, title, body, slug, valid):
    if valid:
        post = post_factory(title, body, slug)
        assert post.title == title
        assert post.body == body
        assert post.slug == slug
    else:
        with pytest.raises(ValidationError):
            post = post_factory(title, body, slug)


def test_post_author(db, post_factory, user):
    post = post_factory(author=user)
    assert post.author == user
    assert post.author.username == "TestUser"


def test_post_dublicate_slug(db, post_factory):
    post_factory(slug="slug")
    with pytest.raises(IntegrityError):
        post_factory(slug="slug")


def test_post_has_timestamps(db, post_factory):
    post = post_factory()
    assert post.created_at is not None
    assert post.updated_at is not None



@pytest.mark.parametrize(
    "title, repr_string",
    [
        ("Test Post", "Test Post"),
        ("სატესტო პოსტი", "სატესტო პოსტი"),
        ("Тестовый пост", "Тестовый пост"),
        ("テスト投稿", "テスト投稿"),
    ]
)
def test_post_str_method(db, post_factory, title, repr_string):
    post = post_factory(title=title)
    assert str(post) == repr_string


def test_post_abs_url(db, post_factory):
    post = post_factory(slug="test-post")
    expected_url = reverse("blog:post-detail", kwargs={"slug": post.slug})
    actual_url = post.get_absolute_url()
    assert actual_url == expected_url


def test_profile_creation(db, user):
    assert user.profile is not None
    assert user.profile.image.name == "default.png"
    assert str(user.profile) == f"{user.username}'s Profile"


def test_profile_img_resize(db, profile_with_img):
    with Image.open(profile_with_img.image.path) as img:
        assert img.width <= 300
        assert img.height <= 300
