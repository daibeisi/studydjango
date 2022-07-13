from django.contrib import admin
from .models import Blog,Category,Tag,BlogUser

# Register your models here.
class BlogAdmin (admin.ModelAdmin):
    list_display=("title","create_time","edit_time","category","author","view",)
# 注册博客，有第二个参数，按照BlogAdmin定义进行管理
admin.site.register(Blog,BlogAdmin)
# 注册BlogUser，默认样式管理
admin.site.register(BlogUser)
admin.site.register(Category)
admin.site.register(Tag)