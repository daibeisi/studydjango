from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=32, verbose_name="团体名称")
    script = models.CharField(max_length=60, blank=True, verbose_name="备注")

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=32, verbose_name="部门名称")
    script = models.CharField(max_length=60, blank=True, verbose_name="备注")

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=32, verbose_name="姓名")
    email = models.EmailField(blank=True, verbose_name="邮箱")
    about = models.TextField(blank=True, verbose_name="简介")
    department = models.ForeignKey(to="Department", on_delete=models.CASCADE, blank=True, verbose_name="部门")
    group = models.ManyToManyField(to="Group", blank=True, verbose_name="小组")
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name="薪水")
    info = models.OneToOneField(to="EmployeeInfo", on_delete=models.CASCADE, null=True, blank=True, verbose_name="员工信息")

    def __str__(self):
        return self.name


class EmployeeInfo(models.Model):
    SHIRT_SIZES = (
        ('XXS', 'XXS'),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('3XL', '3XL'),
    )
    phone = models.CharField(blank=True, max_length=15, verbose_name="电话号码", help_text="请认真核实电话号码是否准确！")
    address = models.CharField(blank=True, max_length=50, verbose_name="地址")
    shirt_size = models.CharField(max_length=3, choices=SHIRT_SIZES, null=True, blank=True, verbose_name="衣服尺码")
