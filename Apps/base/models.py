from django.db import models
from django.contrib.auth.models import User
# from Apps.dep.models import Department
from concurrency.fields import IntegerVersionField
from django.db.models import OuterRef, Subquery
import uuid
import random


class BaseModel(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    edit_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    create_user = models.ForeignKey(verbose_name="创建者", to=User, on_delete=models.CASCADE)
    edit_user = models.ForeignKey(verbose_name="编辑者", to=User, on_delete=models.CASCADE, blank=True, null=True)
    is_delete = models.BooleanField(verbose_name="逻辑删除", default=False)

    # version = IntegerVersionField()

    class Meta:
        # 告诉 Django 这是个抽象基类
        abstract = True

    def save(self, *args, **kwargs):
        # 在这里执行自定义逻辑
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        """重写数据库删除方法实现逻辑删除"""
        self.is_delete = True
        self.save()


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
    uid = models.UUIDField(verbose_name="用户标识码", default=uuid.uuid1, editable=False, db_index=True, unique=True)
    nickname = models.CharField(verbose_name="昵称", max_length=30, blank=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name="用户")
    id_number = models.CharField(verbose_name="身份证号", max_length=30, blank=True, null=True, unique=True)
    openid = models.CharField(verbose_name="微信openid", max_length=30, blank=True, null=True, unique=True)
    unionid = models.CharField(verbose_name="微信unionid", max_length=30, blank=True, null=True, unique=True)
    gender = models.CharField(verbose_name="性别", choices=GenderChoices.choices, max_length=10, blank=True, null=True)
    avatar = models.ImageField(verbose_name="头像", upload_to='avatar', default='avatar/avatar.png', max_length=100)
    birthday = models.DateField(verbose_name="出生日期", blank=True, null=True)
    telephone = models.CharField(verbose_name="座机电话", max_length=15, blank=True, null=True)
    mobile_phone = models.CharField(verbose_name="手机号码", max_length=15, blank=True, null=True)
    dep = models.ForeignKey(verbose_name="所属部门", to="dep.Department", blank=True, null=True,
                            on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.nickname:
            self.nickname = f"用户_{random.choice(letters)}{random.choice(letters)}{random.choice(numbers)}" \
                            f"{random.choice(numbers)}{random.choice(letters)}{random.choice(numbers)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息表"
        ordering = ['id']


class Country(models.Model):
    name = models.CharField(verbose_name="名称", max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '国家'
        verbose_name_plural = '国家列表'


class Province(models.Model):
    name = models.CharField(verbose_name="名称", max_length=30)
    country = models.ForeignKey(verbose_name="国家", to="Country", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '省'
        verbose_name_plural = '省列表'
        unique_together = ("country", "name")


class City(models.Model):
    name = models.CharField(verbose_name="名称", max_length=30)
    country = models.ForeignKey(verbose_name="国家", to="Country", on_delete=models.CASCADE)
    province = models.ForeignKey(verbose_name="省", to="Province", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '市'
        verbose_name_plural = '市列表'
        unique_together = ("country", "province", "name")


class Area(models.Model):
    name = models.CharField(verbose_name="名称", max_length=50)
    country = models.ForeignKey(verbose_name="国家", to="Country", on_delete=models.CASCADE)
    province = models.ForeignKey(verbose_name="省", to="Province", on_delete=models.CASCADE)
    city = models.ForeignKey(verbose_name="市", to="City", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '区/县'
        verbose_name_plural = '区/县列表'
        unique_together = ("country", "province", "city", "name")


class Town(models.Model):
    name = models.CharField(verbose_name="名称", max_length=50)
    country = models.ForeignKey(verbose_name="国家", to="Country", on_delete=models.CASCADE)
    province = models.ForeignKey(verbose_name="省", to="Province", on_delete=models.CASCADE)
    city = models.ForeignKey(verbose_name="市", to="City", on_delete=models.CASCADE)
    area = models.ForeignKey(verbose_name="区/县", to="Area", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '乡/镇/街道'
        verbose_name_plural = '乡/镇/街道列表'
        unique_together = ("country", "province", "city", "area", "name")
