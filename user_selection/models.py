from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    ROLE_CHOICES = [
        ('user','Пользователь'),
        ('manager','Менеджер'),
        ('CRMadmin','CRM-администратор'),
    ]
    username = models.CharField(max_length=50)
    role = models.CharField(max_length=100,choices=ROLE_CHOICES)
    offer = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='static/icons', default='static/icons/default_icon.png', blank=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'role']

    class Meta:
        db_table = 'users'
