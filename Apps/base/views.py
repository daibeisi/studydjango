import json
import time
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.db import transaction
from django.conf.global_settings import LOGIN_URL
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework import permissions

from DjangoProject.tools import mp
from .models import (
    UserInfo,
    Department,
    Router,
    Country,
    Province,
    City,
    Area,
    Town
)
from .serializers import (
    DepartmentSerializer,
    CountrySerializer,
    ProvinceSerializer,
    CitySerializer,
    AreaSerializer,
    TownSerializer
)


class RegisterView(APIView):
    def get(self, request, format=None):
        return render(request, "base/register.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username or not password:
            return Response({"code": -1, "message": "用户名或密码为空！"})
        if User.objects.filter(username=username).exists():
            return Response({"code": -1, "message": "用户已存在！"})
        User.objects.create(username=username, password=make_password(password))
        return Response({"code": 0, "message": "用户创建成功！", "data": {"username": username, "password": password}})


class LoginView(APIView):
    def get(self, request):
        return render(request, "base/login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username or not password:
            return Response({"code": -1, "message": "用户名或密码为空！"})
        user = User.objects.filter(username=username).first()
        if not user:
            return Response({"code": -1, "msg": "系统中未找到该用户！"})
        if not check_password(password, user.password):
            return Response({"code": -1, "msg": "密码错误！"})
        authenticate(request, username=username, password=password)
        return Response({"code": 0, "msg": "登陆成功"})


class LogoutView(APIView):
    def get(self, request):
        request.session.flush()
        return HttpResponseRedirect(LOGIN_URL)

    def post(self, request):
        request.session.flush()
        return Response({"code": 0, "msg": "登出成功"})


class WeixinLogin(APIView):
    def post(self, request, format=None):
        js_code = json.loads(request.body).get('js_code')
        user_id_info = mp.get_user_id_info(js_code)
        openid = user_id_info.get("openid")
        unionid = user_id_info.get("unionid")
        with transaction.atomic():
            if openid:
                user_info = UserInfo.objects.filter(openid=openid).first()
            else:
                user_info = UserInfo.objects.filter(unionid=unionid).first()
            if user_info:
                user = UserInfo.user
            else:
                user = User.objects.create(username=time.time(), password=make_password(time.time()))
                user.userinfo.openid = openid
                user.userinfo.unionid = unionid
                user.userinfo.save()
        refresh = RefreshToken.for_user(user)
        return Response({
                "code": 0,
                "msg": "登陆成功",
                "data": {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token)
                }
            })


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticated,)


@api_view(['GET', 'POST'])
def country_list(request):
    """
    List all countries, or create a new country.
    """
    if request.method == 'GET':
        records = Country.objects.all()
        serializer = CountrySerializer(records, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def country_detail(request, pk):
    """
    Retrieve，update or delete an article instance。"""
    try:
        record = Country.objects.get(pk=pk)
    except Country.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CountrySerializer(record)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CountrySerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProvinceList(generics.ListCreateAPIView):
    queryset = Province.objects.all().order_by('id')
    serializer_class = ProvinceSerializer


class ProvinceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all().order_by('id')
    serializer_class = CitySerializer


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class AreaList(generics.ListCreateAPIView):
    queryset = Area.objects.all().order_by('id')
    serializer_class = AreaSerializer


class AreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class TownList(generics.ListCreateAPIView):
    queryset = Town.objects.all().order_by('id')
    serializer_class = TownSerializer


class TownDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Town.objects.all()
    serializer_class = TownSerializer
