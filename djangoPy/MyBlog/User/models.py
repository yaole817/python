from django.db import models
from django import forms

# Create your models here.

# Create your models here.
class User(models.Model):
    username= forms.CharField(label="用户名", max_length=100)
    password = forms.CharField(label='密码', min_length=8, widget=forms.PasswordInput())

    def __str__(self):
        return self.username
    # class Meta:
    #     ordering = ['-date_time']