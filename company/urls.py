from django.urls import path, re_path
from company.views import *

# 指定命名空间
app_name = "company"

urlpatterns = [
    # 部门管理
    path("list_dep/", list_dep, name="list_dep"),
    re_path("del_dep/(?P<dep_id>[0-9])/", del_dep, name="del_dep"),
    path("add_dep/", add_dep, name="add_dep"),
    re_path("edit_dep/(?P<dep_id>[0-9])/", edit_dep, name="edit_dep"),
    # 员工信息管理
    path("list_employeeinfo/", list_employeeinfo, name="list_employeeinfo"),
    re_path("del_employeeinfo/(?P<employeeinfo_id>[0-9])/", del_employeeinfo, name="del_employeeinfo"),
    path("add_employeeinfo/", add_employeeinfo, name="add_employeeinfo"),
    re_path("edit_employeeinfo/(?P<employeeinfo_id>[0-9])/", edit_employeeinfo, name="edit_employeeinfo"),
    # 员工管理
    path("list_employee/", list_employee, name="list_employee"),
    re_path("del_employee/(?P<employee_id>[0-9])/", del_employee, name="del_employee"),
    path("add_employee/", add_employee, name="add_employee"),
    re_path("edit_employee/(?P<employee_id>[0-9])/", edit_employee, name="edit_employee"),
    # 小组管理
    path("list_group/", list_group, name="list_group"),
    re_path("del_group/(?P<group_id>[0-9])/", del_group, name="del_group"),
    path("add_group/", add_group, name="add_group"),
    re_path("edit_group/(?P<group_id>[0-9])/", edit_group, name="edit_group"),
]
