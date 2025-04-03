from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, userInfo

urlpatterns = [
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('', userInfo, name='home'),
]
