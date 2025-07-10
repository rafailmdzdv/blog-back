from django.db.models import QuerySet
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from posts import models, serializers


class PostsView(generics.ListAPIView):
    serializer_class = serializers.PostSerializer

    def get_queryset(self) -> QuerySet[models.Post]:
        return models.Post.objects.all()


class PostContentView(generics.RetrieveAPIView):
    serializer_class = serializers.PostContentSerializer

    def retrieve(self, _: Request) -> Response:
        obj = models.Post.objects.get(pk=self.request.GET['id'])
        return Response(self.get_serializer(obj).data)
