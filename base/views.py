from django.shortcuts import render, HttpResponse
import datetime


# Create your views here.
def index(request):
    return render(request, "base/index.html")


def test(request):
    return render(request, "base/test.html", {'hi': "你好", 'test': "测试"})


def time(request):
    now = datetime.datetime.now().now()
    # return HttpResponse("<div align='center'><h1>你好，欢迎你浏览本页面</h1><hr>当前时间是{year}年{month}月{day}日{hour}时"
    #                     "{minute}分{second}秒{microsecond}<br></div>".format(year=now.year, month=now.month,
    #                                                                        day=now.day, hour=now.hour,
    #                                                                        minute=now.minute, second=now.second,
    #                                                                        microsecond=now.microsecond))
    return render(request, "base/time.html", {'now': now})


def test_filter(request):
    return render(request, "base/test_filter.html", {'hair': "morehair"})


def test_simpletag(request):
    return render(request, "base/test_tag.html")


def base(request):
    return render(request, "base/base.html")


def inhert_base(request):
    return render(request, "base/inhert_base.html")


def test_include(request):
    return render(request, "base/test_include.html")
