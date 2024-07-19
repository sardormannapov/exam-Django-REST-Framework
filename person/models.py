from django.contrib.auth.models import User
from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField(blank=True, null=True)
    manufacture = models.TextField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey("Category", models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name="Users", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    cat_name = models.CharField(max_length=60)


    def __str__(self):
        return self.cat_name