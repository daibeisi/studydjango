""" Django REST Framework 相关设置

    Django REST Framework 相关设置，配置相关参数供 settings.py 导入引用
"""
from rest_framework import routers
router = routers.DefaultRouter()


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    # 身份认证后端——如果有多个认证，则有一个认证通过就算认证成功
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',  # 基本认证 —— 请求的时候传递用户名和密码，进行身份认证
        # 在drf视图(APIView)处理一个请求的过程中，会提取cookie中的sessionid，并在缓存中获取用户数据
        # 'rest_framework.authentication.SessionAuthentication',  # session认证
        # "rest_framework.authentication.TokenAuthentication",  # Token认证
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT认证
    ),
    # 权限认证后端,有多个权限后端，遵循最严格的
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated', # 只有经过身份认证确定用户身份才能访问
        # 'rest_framework.permissions.IsAdminUser', # is_staff=True才能访问 —— 管理员(员工)权限
        # 'rest_framework.permissions.AllowAny',  # 允许所有
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',  # 有身份 或者 只读访问(self.list,self.retrieve)
    ),
    # 流量限制后端
    'DEFAULT_THROTTLE_CLASSES': (
        # 'rest_framework.throttling.AnonRateThrottle', # 限制匿名用户访问限制
        # 'rest_framework.throttling.UserRateThrottle', # 非匿名用户访问限制
        'rest_framework.throttling.ScopedRateThrottle',  # 自定义限流后端
    ),
    # 流量(请求次数)限制频率
    'DEFAULT_THROTTLE_RATES': {
        'anon': '3/day',  # 匿名用户访问次数     3/day  3/hour  3/second  3/minute
        'user': '5/day',  # 非匿名用户访问次数

        # 自定义限流后端的访问次数规则
        'books': '3/day',
        'heroes': '5/day'
    },
}