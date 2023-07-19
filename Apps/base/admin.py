from django.contrib import admin

from .models import UserInfo, Country, Province, City, Area, Town
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Permission


class UserInfoInline(admin.StackedInline):
    model = UserInfo
    can_delete = False
    verbose_name_plural = "用户信息"


class NewUserAdmin(UserAdmin):
    inlines = (UserInfoInline,)


admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
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