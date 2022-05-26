from django.contrib import admin
from .models import UserInfo


# Register your models here.
# 自定义数据模型在管理后台的显示样式
class UserInfoAdmin(admin.ModelAdmin):
    # 指明在Django Admin管理后台列表模式下显示哪些字段
    list_display = (
        'user',
        'birthdate',
        'phone',
        # 'address'
    )

admin.site.register(UserInfo, UserInfoAdmin)
