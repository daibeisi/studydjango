import os
from datetime import timedelta
from .config import cf


Django_ENV = os.environ.get('Django_ENV', "development")


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=2),  # 访问令牌有效时间
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),  # 刷新令牌有效时间
    "ROTATE_REFRESH_TOKENS": True,  # 若为True，刷新时refresh_token也会刷新
    "BLACKLIST_AFTER_ROTATION": True,  # 若为True，刷新后的token将添加到黑名单中
    "UPDATE_LAST_LOGIN": False,  # 是否更新auth_user 表中的 last_login 字段
    "ALGORITHM": "HS256",  # 加密算法
    "SIGNING_KEY": cf.get(Django_ENV, 'Django_SECRET_KEY'),  # 签名密钥
    "VERIFYING_KEY": "",  # 验证密钥，加密算法指定HMAC时被忽略
    "AUDIENCE": None,  # 生成的令牌中和/或在解码的令牌中验证的受众主张。当设置为 "无 "时，该字段被排除在令牌之外，并且不被验证。
    "ISSUER": None,  # 生成的令牌中和/或在解码的令牌中验证的发行者主张。当设置为 "无 "时，该字段被排除在令牌之外，并且不被验证。
    "JSON_ENCODER": None,
    "JWK_URL": None,  # JWK_URL用于动态解析验证令牌签名所需的公钥
    "LEEWAY": timedelta(seconds=60),  # 令牌过期回旋时间
    "AUTH_HEADER_TYPES": ("Bearer",),  # 需要认证的视图所接受的授权头类型
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",  # 用于认证的授权标头名称
    "USER_ID_FIELD": "id",  # 指定识别用户的字段
    "USER_ID_CLAIM": "user_id",  # 存储用户标识符

    # 确定用户是否被允许进行认证规则
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": (
        "rest_framework_simplejwt.tokens.AccessToken",
        # "rest_framework_simplejwt.tokens.SlidingToken"
    ),  # 允许用来证明认证的令牌类型
    "TOKEN_TYPE_CLAIM": "token_type",  # 存储令牌类型的名称

    # 一个无状态的用户对象，由一个经过验证的令牌支持。仅用于JWTStatelessUserAuthentication认证后端。
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",  # 存储一个令牌的唯一标识符的声称名称

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",  # 存储滑动令牌刷新期的过期时间的名称
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),  # 滑动令牌的有效时间
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),  # 指定了可以刷新滑动令牌的有效时间

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}