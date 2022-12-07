from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login


# Create your views here.
def user_login(request):
    if request.method == "GET":
        return render(request, "base/login.html")
    else:
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                data = {
                    "code": 200,
                    "message": "登陆成功"
                }
            else:
                data = {
                    "code": 401,
                    "message": "用户名或密码出现错误！"
                }
        except Exception as e:
            data = {
                "code": 500,
                "message": "系统错误！"
            }
        return JsonResponse(data)
