import pytest
from django.test.client import Client

from posts.models import Post


@pytest.mark.django_db
def test_list_posts(client: Client, create_posts: None) -> None:
    response = client.get('/api/v1/posts/')

    assert len(response.json()) > 0


@pytest.mark.django_db
def test_post_content(client: Client, post: Post) -> None:
    response = client.get('/api/v1/posts/content/', query_params={'id': post.pk})

    assert response.json()['content'] == post.content
