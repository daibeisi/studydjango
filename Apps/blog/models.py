from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import strip_tags
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="分类名", max_length=30)
    remark = models.TextField(verbose_name="备注", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


class Tag(models.Model):
    name = models.CharField(verbose_name="标签名", max_length=30)
    remark = models.TextField(verbose_name="备注", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Blog(models.Model):
    title = models.CharField(verbose_name="标题", max_length=80)
    body = RichTextUploadingField(config_name='default', verbose_name="内容")
    abstract = models.TextField(verbose_name="摘要", blank=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    edit_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE, verbose_name="分类")
    tags = models.ManyToManyField(to="Tag", blank=True, verbose_name="标签")
    author = models.ForeignKey(to="blog.BlogUser", on_delete=models.CASCADE, verbose_name="作者")
    view = models.IntegerField(default=0, verbose_name="查看次数")

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.pk})

    def increase_view(self):
        """调用save()方法，将查看次数view加1"""
        self.view += 1
        self.save(update_fields=["view"])

    def save(self, *args, **kwargs):
        if not self.abstract:
            self.abstract = strip_tags(self.body)[:118]
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "博文信息"
        verbose_name_plural = "博文信息"
        ordering = ("-create_time",)
        unique_together = ("title", "author")


class BlogUser(AbstractUser):
    nickname = models.CharField(verbose_name="昵称", max_length=30, blank=True)
    telephone = models.CharField(max_length=11, null=True, unique=True)
    avatar = models.ImageField(upload_to="avatar", blank=True, verbose_name="头像")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
