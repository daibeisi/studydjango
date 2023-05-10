from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        verbose_name = "代码片段"
        verbose_name_plural = "代码片段表"
        ordering = ['created']

    def __str__(self):
        return "%s" % self.title

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)


class Class(models.Model):
    name = models.CharField(max_length=30, verbose_name="班级名称")

    class Meta:
        verbose_name = "班级信息"
        verbose_name_plural = "班级信息表"
        ordering = ['id']

    def __str__(self):
        return "%s" % self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False, verbose_name="用户")
    sex = models.IntegerField(db_column='sex', verbose_name="性别", choices=[(0, "女"), (1, "男")])
    owner_class = models.ForeignKey(to="Class", on_delete=models.CASCADE, verbose_name="班级")

    class Meta:
        verbose_name = "学生信息"
        verbose_name_plural = "学生信息表"
        ordering = ['id']

    def __str__(self):
        return "%s" % self.user.username
