import pytest
from django.urls import reverse


@pytest.fixture
def post_added(db, post_factory):
    return post_factory("title", "body", "slug-slug")

@pytest.fixture
def data():
    return {
        "title": "title",
        "body": "body",
        "slug": "slug-slug",
    }


def test_post_list(db, client):
    url = reverse("blog:post-list")
    response = client.get(url)
    assert response.status_code == 200


def test_post_detail(post_added, client):
    url = reverse("blog:post-detail", kwargs={"slug": "slug-slug"})
    response = client.get(url)
    assert response.status_code == 200


def test_post_create(db, client, data):
    url = reverse("blog:post-create")

    response = client.post(url, data)
    
    assert response.status_code == 302
    assert "login" in response.url


def test_post_create_loged_in(db, client, data, user_login):
    url = reverse("blog:post-create")
    response = client.post(url, data)
    
    assert response.status_code == 302
    assert response.url == reverse("blog:post-detail", kwargs={"slug": "slug-slug"})


def test_post_create_no_data(db, client, user_login):
    url = reverse("blog:post-create")
    response = client.post(url)
    
    assert response.status_code == 200


# def test_post_update(db, post_factory, user_login, data, client):
#     post = post_factory(author=user_login, **data)

#     url = reverse("blog:post-update", kwargs={"slug": post.slug})
#     response = client.put(url, data=data)

#     print(response.content.decode())
    
#     assert response.status_code == 302
#     assert response.url == reverse("blog:post-detail", kwargs={"slug": "slug-slug"})