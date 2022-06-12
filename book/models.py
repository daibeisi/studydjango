from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=30, verbose_name="书籍名称")
    about = models.TextField(verbose_name="书籍简介")
    publication_date = models.DateField(verbose_name="出版日期")
    # 外键，多对一关系。设置on_delete=models.CASCADE，表示级联删除，“一”被删除后，“多”也会跟着删除。
    press = models.ForeignKey(to="Press", on_delete=models.CASCADE, verbose_name="出版社")
    author = models.ManyToManyField(to="Author", verbose_name="作者")

    class Meta:
        verbose_name="图书信息"  # 数据模型对象单数名
        verbose_name_plural="图书信息"  # 数据模型对象复数名
        ordering = ("-publication_date", "name")  # 排序方式
        # unique_together = ("name", "author")  # 联合约束

    def __str__(self):
        return self.name + "--相关图书信息"


class Press(models.Model):
    name = models.CharField(max_length=30, verbose_name="出版社名称")
    address = models.TextField(verbose_name="出版社地址")

    class Meta:
        verbose_name = "出版社信息"
        verbose_name_plural = "出版社信息"

    def __str__(self):
        return "社名：" + self.name


class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name="作者姓名")
    avatar = models.ImageField(verbose_name="作者头像")
    email = models.EmailField(verbose_name="邮箱")
    birthday = models.DateField(verbose_name="出生日期")

    class Meta:
        verbose_name = "作者信息"
        verbose_name_plural = "作者信息"

    def __str__(self):
        return "作者：" + self.name