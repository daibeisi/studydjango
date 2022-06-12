from django.contrib import admin
from book.models import Book, Press, Author
from django.utils.safestring import mark_safe

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = "publication_date"  # 用出版日期作为导航栏查询字段
    empty_value_display = "-无值-"  # 设置字段无值时显示的内容
    filter_horizontal = ("author",)  # 设置author字段的选择方式为水平扩展选择
    # 以下代码在页面上对字段进行分组显示或布局
    fieldsets = (
        ("图书信息", {
            'fields': (("name", "publication_date"), "press", "author")
        }),
        ('图书简介', {
            'classes': ('collapse',),
            'fields': ('about',),
        }),
    )
    # 自定义一个字段
    def about_str(self,obj):
        return obj.about[:20]  # 对字段进行切片，取前20个字符
    # 设置自定义字段名字
    about_str.short_description = "简介"
    # 设置过滤导航栏字段
    list_filter = ("name", "press", "author")
    # 设置查询字段
    search_fields = ("name", "press__name", "author__name")
    # 列表显示字段
    list_display = ("name", "about_str", "publication_date", "press")  # TODO:列表如何展示多对多字段作者
    # 连接修改页面字段
    list_display_links = ("name",)
    # 指定列表页面可被编辑字段
    list_editable = ("publication_date",)
    # 显示查询到的记录数
    show_full_result_count = True
    # 设定每页显示记录数
    list_per_page = 10
    # 外键字段或choices集合更改默认<select>标签为<radio>标签
    radio_fields = {"press": admin.VERTICAL}

    # 定义批处理方法
    def chang_press(self,request,queryset):
        press_set = Press.objects.filter(name="呆贝斯出版社")
        if press_set.exists():
            rows = queryset.update(press=press_set[0])
            self.message_user(request, '%s条记录被修改成“呆贝斯出版社”'%rows)
        else:
            self.message_user(request, "未查询到“呆贝斯出版社”，更改不成功")
    chang_press.short_description = '选中记录的出版社改为“呆贝斯出版社”'
    actions = ['chang_press']


admin.site.register(Book, BookAdmin)


class PressAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    list_per_page = 10


admin.site.register(Press, PressAdmin)


class AuthorAdmin(admin.ModelAdmin):
    def avatar_data(self,obj):
        return mark_safe('<img src="/upload/{avatar}" width="50px" height="30px"/>'.format(avatar=obj.avatar))
    avatar_data.short_description = "头像"
    list_display = ("name", "email", "birthday", "avatar_data")
    list_per_page = 10


admin.site.register(Author, AuthorAdmin)

