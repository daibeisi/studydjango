import logging
from django.shortcuts import render, redirect
from company.models import *

# Get an instance of a logger
logging.basicConfig(format='%(asctime)s-%(levelname)s-%(pathname)s[%(lineno)d]: %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Create your views here.
def list_dep(request):
    dep_list = Department.objects.all()
    return render(request, 'company/dep_list.html', {'dep_list': dep_list})


def del_dep(request, dep_id):
    dep = Department.objects.get(id=dep_id)
    dep.delete()
    return redirect("/company/list_dep/")


def add_dep(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        script = request.POST.get("script")
        if name.strip() == "":
            return render(request, "company/dep_list.html", {"error": "部门名称不能为空"})
        try:
            Department.objects.create(name=name, script=script)
            # dep = Department(name=name, script=script)
            # dep.save()
            # dic = {"name": name, "script": script}
            # Department.objects.create(**dic)
        except Exception as e:
            logger.error(e)
            return render(request, "company/dep_list.html", {"error": "部门创建失败"})
        else:
            return redirect("/company/list_dep/")
    return render(request, "company/dep_add.html")


def edit_dep(request, dep_id):
    dep = Department.objects.get(id=dep_id)
    if request.method == 'POST':
        name = request.POST.get("name")
        script = request.POST.get("script")
        dep.name = name
        dep.script = script
        dep.save()
        return redirect("/company/list_dep/")
    else:
        return render(request, "company/dep_edit.html", {"dep": dep})


def list_group(request):
    group_list = Group.objects.all()
    return render(request, 'company/group_list.html', {'group_list': group_list})


def del_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group.delete()
    return redirect("/company/list_group/")


def add_group(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        script = request.POST.get("script")
        if name.strip() == "":
            return render(request, "company/group_list.html", {"error": "小组名称不能为空"})
        try:
            Group.objects.create(name=name, script=script)
            # dep = Department(name=name, script=script)
            # dep.save()
            # dic = {"name": name, "script": script}
            # Department.objects.create(**dic)
        except Exception as e:
            logger.error(e)
            return render(request, "company/group_list.html", {"error": "小组创建失败"})
        else:
            return redirect("/company/list_group/")
    return render(request, "company/group_add.html")


def edit_group(request, group_id):
    if request.method == 'POST':
        name = request.POST.get("name")
        script = request.POST.get("script")
        group = Group.objects.get(id=group_id)
        group.name = name
        group.script = script
        group.save()
        return redirect("/company/list_group/")
    else:
        group = Group.objects.get(id=group_id)
        return render(request, "company/group_edit.html", {"group": group})


def list_employee(request):
    employee_list = Employee.objects.all()
    return render(request, 'company/employee_list.html', {'employee_list': employee_list})


def del_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return redirect("/company/list_employee/")


def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        # about = request.POST.get("about")
        department = request.POST.get("dep")
        employee_info = request.POST.get("employeeinfo")
        salary = request.POST.get("salary")
        groups = request.POST.getlist("group")  # 取得多个值
        try:
            employee = Employee.objects.create(name=name, email=email, salary=float(salary),
                                               department_id=department, info_id=employee_info)
            employee.group.set(groups)
        except Exception as e:
            logger.error(e)
            group_list = Group.objects.all()
            dep_list = Department.objects.all()
            employeeinfo_list = Employee.objects.all()
            return render(request, "company/employee_add.html", {"group_list": group_list, "dep_list": dep_list,
                                                                 "employeeinfo_list": employeeinfo_list,
                                                                 "error": "员工创建失败"})
        else:
            return redirect("/company/list_employee/")
    group_list = Group.objects.all()
    dep_list = Department.objects.all()
    employeeinfo_list = Employee.objects.all()
    return render(request, "company/employee_add.html", {"group_list": group_list, "dep_list": dep_list,
                                                         "employeeinfo_list": employeeinfo_list})


def edit_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        about = request.POST.get("about")
        department = request.POST.get("department")
        salary = request.POST.get("salary")
        info = request.POST.get("info")
        groups = request.POST.getlist("group")  # 取得多个值
        employee.name = name
        employee.email = email
        employee.about = about
        employee.department = department
        employee.salary = salary
        employee.info = info
        employee.group.set(groups)
        employee.save()
        return redirect("/company/list_employee/")
    else:
        group_list = Group.objects.all()
        dep_list = Department.objects.all()
        employeeinfo_list = Employee.objects.all()
        return render(request, "company/employee_edit.html", {"group_list": group_list, "dep_list": dep_list,
                                                             "employeeinfo_list": employeeinfo_list,
                                                             "employee": employee})


def list_employeeinfo(request):
    employeeinfo_list = EmployeeInfo.objects.all()
    return render(request, 'company/employeeinfo_edit.html', {'employeeinfo_list': employeeinfo_list})


def add_employeeinfo(request):
    if request.method == 'POST':
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        try:
            EmployeeInfo.objects.create(phone=phone, address=address)
        except Exception as e:
            logger.error(e)
            return render(request, "company/employeeinfo_list.html", {"error": "员工信息创建失败"})
        else:
            return redirect("/company/list_employeeinfo/")
    return render(request, "company/employeeinfo_add.html")


def del_employeeinfo(request, employeeinfo_id):
    employeeinfo = EmployeeInfo.objects.get(id=employeeinfo_id)
    employeeinfo.delete()
    return redirect("/company/list_employeeinfo/")


def edit_employeeinfo(request, employeeinfo_id):
    employeeinfo = EmployeeInfo.objects.get(id=employeeinfo_id)
    if request.method == 'POST':
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        employeeinfo.phone = phone
        employeeinfo.address = address
        employeeinfo.save()
        return redirect("/company/list_employeeinfo/")
    else:
        return render(request, "company/employeeinfo_edit.html", {"employeeinfo": employeeinfo})
