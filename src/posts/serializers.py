import base64
import zlib

from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    icon_name = serializers.CharField(source='icon.name')

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'description',
            'icon_name',
            'created',
        )


class PostContentSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField('compressed_content')

    class Meta:
        model = Post
        fields = ('content',)

    def compressed_content(self, obj: Post) -> bytes:
        return base64.b64encode(zlib.compress(obj.content.encode('utf-8')))
