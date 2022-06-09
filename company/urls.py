from django.urls import path, re_path
from company.views import *

# 指定命名空间
app_name = "company"

urlpatterns = [
    path("", index, name="company_index"),
    # 部门管理
    path("list_dep/", list_dep, name="list_dep"),
    path("del_dep/<int:dep_id>/", del_dep, name="del_dep"),
    path("add_dep/", add_dep, name="add_dep"),
    path("edit_dep/<int:dep_id>/", edit_dep, name="edit_dep"),
    # 员工信息管理
    path("list_employeeinfo/", list_employeeinfo, name="list_employeeinfo"),
    path("del_employeeinfo/<int:employeeinfo_id>/", del_employeeinfo, name="del_employeeinfo"),
    path("add_employeeinfo/", add_employeeinfo, name="add_employeeinfo"),
    path("edit_employeeinfo/<int:employeeinfo_id>/", edit_employeeinfo, name="edit_employeeinfo"),
    # 员工管理
    path("list_employee/", list_employee, name="list_employee"),
    path("del_employee/<int:employee_id>/", del_employee, name="del_employee"),
    path("add_employee/", add_employee, name="add_employee"),
    path("edit_employee/<int:employee_id>/", edit_employee, name="edit_employee"),
    # 小组管理
    path("list_group/", list_group, name="list_group"),
    path("del_group/<int:group_id>/", del_group, name="del_group"),
    path("add_group/", add_group, name="add_group"),
    path("edit_group/<int:group_id>/", edit_group, name="edit_group"),
    # 测试forms
    path("test_forms/", test_forms, name="test_forms"),
]
