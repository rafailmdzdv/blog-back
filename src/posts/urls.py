from django.urls import path

from posts import views

urlpatterns = (
    path('', views.PostsView.as_view()),
    path('content/', views.PostContentView.as_view()),
)
