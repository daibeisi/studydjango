from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    # TODO:解决测试环境访问图片地址报404
    return render(request, "base/index.html")


def test(request):
    return render(request, "base/test.html", {'hi': "你好", 'test': "测试"})
