from django.db import models
from django.contrib.auth.models import User


class BBS(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey('BBS_user', on_delete=models.CASCADE)
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    administrator = models.ForeignKey('BBS_user', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BBS_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    signature = models.CharField(max_length=128, default='This guy is too lazy to leave anything here.')
    photo = models.ImageField(upload_to="upload_imgs/", default="upload_imgs/user-1.jpg")

    def __str__(self):
        return self.user.username
