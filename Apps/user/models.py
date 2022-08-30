from django.db import models
from django.contrib.auth.models import User
# 引入内置信号
from django.db.models.signals import post_save
# 引入信号接收器的装饰器
from django.dispatch import receiver


# Create your models here.
class UserInfo(models.Model):
    # 字段
    user = models.OneToOneField(to='User', on_delete=models.CASCADE, verbose_name='用户')
    birthdate = models.DateField(blank=True, null=True, verbose_name='出生日期')
    phone = models.CharField(max_length=20, blank=True, default='', verbose_name='电话号码')
    address = models.CharField(max_length=50, blank=True, default='', verbose_name='地址')

    # 信号接收函数，每当新建 User 实例时自动调用
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserInfo.objects.create(user=instance)

    # 信号接收函数，每当更新 User 实例时自动调用
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    class Meta:
        verbose_name = '用户信息'  # 模型对象的单数名，不指定，默认用小写的数据模型名，如数据模型book的单数名默认为book
        verbose_name_plural = '用户信息'  # 模型对象的复数名，中文通常不区分单复数，可以和verbose_name一样。默认是verbose_name加上“s”
        ordering = ('user',)  # 指定的排序方式，接受字段名组成的元祖或列表，字段名前加“-”表示倒序，不加表示正序

    def __str__(self):
        return "用户信息"
