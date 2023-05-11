from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    edit_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    class Meta:
        # 告诉 Django 这是个抽象基类
        abstract = True

    def save(self, *args, **kwargs):
        # 在这里执行自定义逻辑
        super().save(*args, **kwargs)


class GenderChoices(models.TextChoices):
    Female = "female", "女",
    Male = 'male', "男"
    Other = "other", "其他"


class UserInfo(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name="用户")
    id_number = models.CharField(verbose_name="身份证号", max_length=30, blank=True, null=True, unique=True)
    openid = models.CharField(verbose_name="微信openid", max_length=100, blank=True, null=True, unique=True)
    unionid = models.CharField(verbose_name="微信unionid", max_length=100, blank=True, null=True, unique=True)
    gender = models.CharField(verbose_name="性别", max_length=10, choices=GenderChoices.choices, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar', max_length=100, default='avatar/avatar.png', verbose_name="头像")
    birthday = models.DateField(verbose_name="出生日期", blank=True, null=True)
    telephone = models.CharField(verbose_name="座机电话", max_length=20, blank=True, null=True)
    mobile_phone = models.CharField(verbose_name="手机号码", max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}的用户信息"

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息表"
        ordering = ['id']


@receiver(post_save, sender=User)
def create_user_userinfo(sender, instance, created, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_userinfo(sender, instance, **kwargs):
    instance.userinfo.save()