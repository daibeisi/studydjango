import random
import uuid

from django.conf import settings
from django.contrib.auth.models import User, Group, Permission
from django.db import models
from django.db.models.signals import post_save
from django.db.utils import IntegrityError
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ModelLogicalDeleteMixin(models.Model):
    """
    An abstract base class model that provides a logical deletion field and methods.
    """
    is_deleted = models.BooleanField(_("Deleted"), default=False)
    deleted_at = models.DateTimeField(_("Deleted at"), null=True, blank=True)
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Deleted by"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='deleted_%(class)ss'
    )

    class Meta:
        # Tell Django that it's an abstract base class
        abstract = True

    def delete(self, using=None, keep_parents=False, user=None):
        """
        Override the database delete method to implement soft deletion.
        """
        self.is_deleted = True
        self.deleted_at = timezone.now()
        if user:
            self.deleted_by = user
        try:
            self.save()
        except IntegrityError as e:
            # Handle potential integrity errors (e.g., foreign key constraints)
            raise Exception("Failed to perform soft deletion due to an integrity error.") from e

    def hard_delete(self, using=None, keep_parents=False):
        """
        Perform a hard delete of the object.
        """
        super().delete(using=using, keep_parents=keep_parents)


class ModelOptimisticLockMixin(models.Model):
    """
    A mixin that provides optimistic locking for Django models.
    """
    version = models.IntegerField(verbose_name=_("Version"), default=1)

    class Meta:
        # Tell Django that it's an abstract base class
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk:
            # Retrieve the current version of the object from the database
            original = self.__class__.objects.get(pk=self.pk)
            if original.version != self.version:
                raise Exception("This record has been modified by another process.")
            else:
                super().save(*args, **kwargs)
                self.version += 1
        else:
            super().save(*args, **kwargs)


class ModelTraceInfoMixin(models.Model):
    """
    An abstract base class model that provides fields for tracking creation and modification information.
    """
    create_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Creator"),
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_%(class)ss'
    )
    create_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    update_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Editor"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='edited_%(class)ss'
    )
    update_at = models.DateTimeField(_("Last edited at"), auto_now=True)

    class Meta:
        # Tell Django that it's an abstract base class
        abstract = True

    def save(self, user=None, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.pk:  # If the object is being created
            if user:
                self.create_user = user
                self.edit_user = user
        else:  # If the object is being updated
            if user:
                self.edit_user = user
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


class GenderChoices(models.TextChoices):
    Female = "female", "女",
    Male = 'male', "男"
    Other = "other", "其他"


class UserInfo(ModelLogicalDeleteMixin, ModelTraceInfoMixin, ModelOptimisticLockMixin, models.Model):
    user = models.OneToOneField(verbose_name="用户", to=User, on_delete=models.CASCADE, null=True)
    uid = models.UUIDField(verbose_name="用户标识码", default=uuid.uuid1, editable=False, db_index=True, unique=True)
    nickname = models.CharField(verbose_name="昵称", max_length=64, blank=True)
    id_number = models.CharField(verbose_name="身份证号", max_length=64, blank=True, null=True, unique=True)
    openid = models.CharField(verbose_name="微信openid", max_length=64, blank=True, null=True, unique=True)
    unionid = models.CharField(verbose_name="微信unionid", max_length=64, blank=True, null=True, unique=True)
    gender = models.CharField(verbose_name="性别", choices=GenderChoices.choices, max_length=64, blank=True, null=True)
    avatar = models.ImageField(verbose_name="头像", upload_to='avatar', default='avatar/avatar.png', max_length=255)
    birthday = models.DateField(verbose_name="出生日期", blank=True, null=True)
    telephone = models.CharField(verbose_name="座机电话", max_length=32, blank=True, null=True)
    mobile_phone = models.CharField(verbose_name="手机号码", max_length=32, blank=True, null=True)
    dep = models.ForeignKey(verbose_name="所属部门", to="Department", blank=True, null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.nickname:
            letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                       'H', 'I', 'J', 'K', 'L', 'M', 'N',
                       'O', 'P', 'Q', 'R', 'S', 'T',
                       'U', 'V', 'W', 'X', 'Y', 'Z',
                       'a', 'b', 'c', 'd', 'e', 'f', 'g',
                       'h', 'i', 'j', 'k', 'l', 'm', 'n',
                       'o', 'p', 'q', 'r', 's', 't',
                       'u', 'v', 'w', 'x', 'y', 'z']
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
            self.nickname = f"用户_{random.choice(letters)}{random.choice(letters)}{random.choice(numbers)}" \
                            f"{random.choice(numbers)}{random.choice(letters)}{random.choice(numbers)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "人员"
        verbose_name_plural = "人员列表"
        ordering = ['id']


@receiver(post_save, sender=User, dispatch_uid="user_post_save_handler")
def user_post_save_handler(sender, **kwargs):
    user, created = kwargs["instance"], kwargs["created"]
    if created and user.username != settings.ANONYMOUS_USER_NAME:
        UserInfo.objects.create(user=user)
    else:
        try:
            user.userinfo.id
            if user.userinfo.has_changed():
                user.userinfo.save()
        except UserInfo.DoesNotExist:
            UserInfo.objects.create(user=user)


class Company(ModelTraceInfoMixin, ModelOptimisticLockMixin, ModelLogicalDeleteMixin, models.Model):
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


class Department(ModelTraceInfoMixin, ModelOptimisticLockMixin, ModelLogicalDeleteMixin, models.Model):
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
