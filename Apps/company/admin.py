from django.contrib import admin
from .models import *

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    # 指明在Django Admin管理后台列表模式下显示哪些字段
    list_display = (
        'name',
        'email',
        'about',
        'department',
        'salary',
        'info',
    )


admin.site.register(Employee, EmployeeAdmin)


@admin.register(Department, Group, EmployeeInfo)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]
