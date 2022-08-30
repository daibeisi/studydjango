# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
#
# class User(AbstractUser):
#     nickname = models.CharField(verbose_name="昵称", max_length=30, blank=True)
#     telephone = models.CharField(max_length=11, null=True, unique=True)
#     avatar = models.ImageField(upload_to="avatar", blank=True, verbose_name="头像")
#
#     def __str__(self):
#         return self.username
#
#     class Meta:
#         verbose_name = "用户表"
#         verbose_name_plural = verbose_name