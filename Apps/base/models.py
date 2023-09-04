from django.db import models
from django.contrib.auth.models import User, Group, Permission
from concurrency.fields import IntegerVersionField
from django.db.models import OuterRef, Subquery
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from guardian.shortcuts import assign_perm
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
import random


class ModelLogicalDeleteMixin(models.Model):
    is_delete = models.BooleanField(verbose_name="逻辑删除", default=False)

    class Meta:
        # 告诉 Django 这是个抽象基类
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """重写数据库删除方法实现逻辑删除"""
        self.is_delete = True
        self.save()


class ModelTraceInfoMixin(models.Model):
    # Translations: 模型记录日志的翻译
    create_user = models.ForeignKey(verbose_name=_("创建者"), to=User, on_delete=models.SET_NULL, null=True)
    create_time = models.DateTimeField(verbose_name=_("创建时间"), auto_now_add=True)
    edit_user = models.ForeignKey(verbose_name=_("编辑者"), to=User, on_delete=models.SET_NULL, null=True)
    edit_time = models.DateTimeField(verbose_name=_("修改时间"), auto_now=True)

    class Meta:
        # 告诉 Django 这是个抽象基类
        abstract = True

    def save(self, *args, **kwargs):
        # FIXME：修复无法记录当前记录创建者和修改者
        super().save(*args, **kwargs)


class BaseModel(ModelLogicalDeleteMixin, ModelTraceInfoMixin):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    # version = IntegerVersionField()

    class Meta:
        # 告诉 Django 这是个抽象基类
        abstract = True


class GenderChoices(models.TextChoices):
    Female = "female", "女",
    Male = 'male', "男"
    Other = "other", "其他"


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


class UserInfo(models.Model):
    user = models.OneToOneField(verbose_name="用户", to=User, on_delete=models.CASCADE, null=True)
    uid = models.UUIDField(verbose_name="用户标识码", default=uuid.uuid1, editable=False, db_index=True, unique=True)
    nickname = models.CharField(verbose_name="昵称", max_length=30, blank=True)
    id_number = models.CharField(verbose_name="身份证号", max_length=30, blank=True, null=True, unique=True)
    openid = models.CharField(verbose_name="微信openid", max_length=30, blank=True, null=True, unique=True)
    unionid = models.CharField(verbose_name="微信unionid", max_length=30, blank=True, null=True, unique=True)
    gender = models.CharField(verbose_name="性别", choices=GenderChoices.choices, max_length=10, blank=True, null=True)
    avatar = models.ImageField(verbose_name="头像", upload_to='avatar', default='avatar/avatar.png', max_length=100)
    birthday = models.DateField(verbose_name="出生日期", blank=True, null=True)
    telephone = models.CharField(verbose_name="座机电话", max_length=15, blank=True, null=True)
    mobile_phone = models.CharField(verbose_name="手机号码", max_length=15, blank=True, null=True)
    dep = models.ForeignKey(verbose_name="所属部门", to="Department", blank=True, null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.nickname:
            self.nickname = f"用户_{random.choice(letters)}{random.choice(letters)}{random.choice(numbers)}" \
                            f"{random.choice(numbers)}{random.choice(letters)}{random.choice(numbers)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "人员"
        verbose_name_plural = "人员列表"
        ordering = ['id']


@receiver(post_save, sender=UserInfo, dispatch_uid="userinfo_post_save_handler")
def user_post_save_handler(sender, **kwargs):
    userinfo, created = kwargs["instance"], kwargs["created"]
    if created:
        User.objects.create(userinfo=userinfo)
    else:
        userinfo.user.save()


@receiver(post_save, sender=User, dispatch_uid="user_post_save_handler")
def user_post_save_handler(sender, **kwargs):
    user, created = kwargs["instance"], kwargs["created"]
    if created and user.username != settings.ANONYMOUS_USER_NAME:
        UserInfo.objects.create(user=user)
    else:
        user.userinfo.save()


class Company(models.Model):
    name = models.CharField(verbose_name="名称", max_length=30)
    unicode = models.CharField(verbose_name="统一社会信用代码", max_length=30, blank=True, null=True)
    telephone = models.CharField(verbose_name="座机电话", max_length=15, blank=True, null=True)
    mobile_phone = models.CharField(verbose_name="手机号码", max_length=15, blank=True, null=True)
    email = models.CharField(verbose_name="邮箱", max_length=30, blank=True, null=True)
    remark = models.CharField(verbose_name="备注", max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '公司'
        verbose_name_plural = '公司列表'
        unique_together = ("name",)


class Department(models.Model):
    parent = models.ForeignKey(verbose_name="上级部门", to="Department", blank=True, null=True,
                               on_delete=models.SET_NULL)
    name = models.CharField(verbose_name="部门名称", max_length=30)
    manager = models.ForeignKey(verbose_name="部门负责人", to=UserInfo, blank=True, null=True,
                                on_delete=models.SET_NULL)
    telephone = models.CharField(verbose_name="座机电话", max_length=15, blank=True, null=True)
    mobile_phone = models.CharField(verbose_name="手机号码", max_length=15, blank=True, null=True)
    email = models.CharField(verbose_name="部门邮箱", max_length=30, blank=True, null=True)
    sequence = models.IntegerField(verbose_name="排序", default=1)
    active = models.BooleanField(verbose_name="部门状态", default=True)
    remark = models.CharField(verbose_name="备注", max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = '部门列表'
        unique_together = ("parent", "name")


class Router(models.Model):
    parent = models.ForeignKey(verbose_name="上级路由", to="Router", blank=True, null=True,
                               on_delete=models.SET_NULL)
    name = models.CharField(verbose_name="名称", max_length=30, unique=True)
    content = models.JSONField(verbose_name="内容")
    groups = models.ManyToManyField(Group, verbose_name="组", blank=True)
    permissions = models.ManyToManyField(Permission, verbose_name="页面权限", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "路由"
        verbose_name_plural = "路由列表"


class Country(models.Model):
    name = models.CharField(verbose_name="名称", max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '国家'
        verbose_name_plural = '国家列表'


class Province(models.Model):
    name = models.CharField(verbose_name="名称", max_length=30)
    country = models.ForeignKey(verbose_name="国家", to="Country", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '省'
        verbose_name_plural = '省列表'
        unique_together = ("country", "name")


class City(models.Model):
    name = models.CharField(verbose_name="名称", max_length=30)
    province = models.ForeignKey(verbose_name="省", to="Province", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '市'
        verbose_name_plural = '市列表'
        unique_together = ("province", "name")


class Area(models.Model):
    name = models.CharField(verbose_name="名称", max_length=50)
    city = models.ForeignKey(verbose_name="市", to="City", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '区/县'
        verbose_name_plural = '区/县列表'
        unique_together = ("city", "name")


class Town(models.Model):
    name = models.CharField(verbose_name="名称", max_length=50)
    area = models.ForeignKey(verbose_name="区/县", to="Area", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '乡/镇/街道'
        verbose_name_plural = '乡/镇/街道列表'
        unique_together = ("area", "name")
