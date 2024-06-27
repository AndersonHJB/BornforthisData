from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    # 这里使用 Django 内置的 AbstractUser 作为基类，可以继承它的所有属性和方法
    # 如果需要添加额外的用户属性，可以在这里定义新的字段
    pass
