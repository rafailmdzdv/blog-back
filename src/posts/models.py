import base64
import uuid
import zlib
from typing import Any

from django.db import models
from django.db.backends.base.base import BaseDatabaseWrapper


class CompressedTextField(models.TextField):
    def from_db_value(self, value: str, expression: models.CharField, connection: BaseDatabaseWrapper) -> str:  # noqa: ARG002
        if not value:
            return value
        return zlib.decompress(base64.b64decode(value)).decode('utf-8')


class Post(models.Model):
    id = models.UUIDField('Identifier', primary_key=True, default=uuid.uuid4)
    title = models.CharField('Title', max_length=64)
    description = models.CharField('Description', max_length=128)
    content = CompressedTextField('Content (org)')
    created = models.DateTimeField('Created', auto_now_add=True)

    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self) -> str:
        return str(self.title)

    def save(self, **kwargs: dict[str, Any]) -> None:  # type: ignore
        self.content = base64.b64encode(zlib.compress(self.content.encode('utf-8'))).decode('utf-8')
        return super().save(**kwargs)  # type: ignore
