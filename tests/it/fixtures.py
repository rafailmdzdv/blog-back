import pytest
from mixer.backend.django import mixer

from posts.models import Post


@pytest.fixture
def create_posts() -> None:
    mixer.cycle().blend(Post)


@pytest.fixture
def post() -> Post | None:
    return mixer.blend(Post)
