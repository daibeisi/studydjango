from django.contrib import admin

from .models import UserInfo
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserInfoInline(admin.StackedInline):
    model = UserInfo
    can_delete = False
    verbose_name_plural = "用户信息"


class NewUserAdmin(UserAdmin):
    inlines = (UserInfoInline,)


admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
