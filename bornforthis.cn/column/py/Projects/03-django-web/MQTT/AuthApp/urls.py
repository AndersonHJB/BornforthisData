from django.urls import path
from .views import register, login_view

urlpatterns = [
    path('register/', register, name='register'),  # 注册页面 URL
    path('login/', login_view, name='login'),  # 登录页面 URL
]
