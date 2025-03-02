from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("Blog.urls"), name="home"),
    path("", home, name="home"),
    path("user/", include("Users.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
