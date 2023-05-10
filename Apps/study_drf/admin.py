from django.contrib import admin
from .models import Snippet, Student, Class

# Register your models here.
# 注册BlogUser，默认样式管理
admin.site.register(Snippet)
admin.site.register(Student)
admin.site.register(Class)
