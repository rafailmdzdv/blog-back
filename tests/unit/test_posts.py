import base64
import zlib

import pytest

from posts.models import Post


@pytest.mark.django_db
def test_post_creating() -> None:
    content = '\n'.join(
        (
            '* Test headline 1',
            '',
            'There is test text',
        ),
    )
    post = Post.objects.create(title='Test', description='Test post', content=content)

    assert zlib.decompress(base64.b64decode(post.content)).decode('utf-8') == content
