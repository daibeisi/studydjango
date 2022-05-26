from django.contrib import admin


# Register your models here.
class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',  'status', 'mod_date',)  # 设置列表可显示的字段
    list_filter = ()  # 设置过滤选项
    list_per_page = 5  # 每页显示条目数
    list_editable = ()  # 设置可编辑字段
    date_hierarchy = 'id'  # 按日期月份筛选
    ordering = ('-create_time',)  # 按发布日期排序