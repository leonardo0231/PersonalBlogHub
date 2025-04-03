from django.urls import path
from .views import Home, create_post

urlpatterns = [
    path("", Home, name="Home"),
    path("create", create_post),
]
