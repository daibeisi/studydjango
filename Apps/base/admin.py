from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from . import models


class UserInfoInline(admin.StackedInline):
    model = models.UserInfo
    can_delete = False
    verbose_name_plural = "用户信息"


class NewUserAdmin(UserAdmin):
    inlines = (UserInfoInline,)


admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
