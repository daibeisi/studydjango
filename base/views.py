from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hell World!</h1>")


def test(request):
    return render(request, "base/test.html", {'hi': "你好", 'test': "测试"})
