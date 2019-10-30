from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, upload_to="uploads")
    location = models.CharField(blank=True, max_length=100)

    def __str__(self):
        self.user


class Products(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='', blank=False)
    code = models.TextField()
    picture = models.ImageField(blank=False, upload_to="productImage")
    cost = models.CharField(max_length=100, blank=True, default='')
    category = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        self.name

    class Meta:
        ordering = ('name',)
