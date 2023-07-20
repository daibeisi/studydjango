from django.db import models
from Apps.base.models import UserInfo


class Department(models.Model):
    parent = models.ForeignKey(verbose_name="上级部门", to="Department", blank=True, null=True,
                               on_delete=models.CASCADE)
    name = models.CharField(verbose_name="部门名称", max_length=30)
    manager = models.ForeignKey(verbose_name="部门负责人", to=UserInfo, blank=True, null=True,
                                on_delete=models.CASCADE)
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
