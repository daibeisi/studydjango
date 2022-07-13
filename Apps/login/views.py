from django.shortcuts import render, redirect
from django.http import JsonResponse


# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, "login/login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "admin" and password == "123456":
            data = {
                "code": 200,
                "message": "登陆成功"
            }
        else:
            data = {
                "code": 401,
                "message": "用户名或密码出现错误！"
            }
        return JsonResponse(data)
