from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Permission
from guardian.models import GroupObjectPermission, UserObjectPermission
from guardian.admin import GuardedModelAdmin


from .models import (
    UserInfo,
    Department,
    Router,
    Country,
    Province,
    City,
    Area,
    Town
)


class UserInfoInline(admin.StackedInline):
    model = UserInfo
    can_delete = False
    verbose_name_plural = "用户信息"


class NewUserAdmin(UserAdmin):
    inlines = (UserInfoInline,)


admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Router)
class RouterAdmin(admin.ModelAdmin):
    filter_horizontal = ("groups", "permissions")


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass


@admin.register(UserObjectPermission)
class UserObjectPermissionAdmin(GuardedModelAdmin):
    pass


@admin.register(GroupObjectPermission)
class GroupObjectPermissionAdmin(GuardedModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    pass