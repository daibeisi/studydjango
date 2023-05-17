"""
Django settings for DjangoProject project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
# TODO:因为设置文件包含敏感信息，应该尽一切努力限制对它的访问。例如，更改其文件权限，以便只有您和您的 Web 服务器的用户可以读取它。
import os
from pathlib import Path
from .config import cf
from .simpleui import *
from .ckeditor import *
from .rest_framework import REST_FRAMEWORK
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition
INSTALLED_APPS = [
    "simpleui",
    # 默认应用，为了方便大多数项目，如果不需要某个或某些应用，你可以在运行 migrate 前毫无顾虑注释或者删除掉它们
    "django.contrib.admin",  # 管理员站点
    "django.contrib.auth",  # 认证授权系统
    "django.contrib.contenttypes",  # 内容类型框架
    "django.contrib.sessions",  # 会话框架
    "django.contrib.messages",  # 消息框架
    "django.contrib.staticfiles",  # 管理静态文件的框架
    # 第三方应用
    'ckeditor',
    'ckeditor_uploader',
    'haystack',
    'rest_framework',
    # 自定义应用
    "Apps.base"
]

# 设置认证系统中使用的用户模型, 例如这里指定为使用base应用程序中User模型
# AUTH_USER_MODEL = "Apps.base.User"

# 中间件，响应前自动处理
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 自定义中间件
    'middlewares.test_middleware.TestMiddleware'
]

# 指项目文件下同名文件夹下的urls，项目改名字这里也要改
ROOT_URLCONF = "DjangoProject.urls"

# 指定模板路径 BASE_DIR是项目根路径，有别的模板也要加进来
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            # 添加如下配置，即可不用每个模板中添加{% load static %}
            "builtins": [
                "django.templatetags.static"
            ],
        },
    },
]

WSGI_APPLICATION = "DjangoProject.wsgi.application"

Django_ENV = os.environ.get('Django_ENV', "development")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
if Django_ENV == "production":
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = cf.get(Django_ENV, 'Django_SECRET_KEY')

    # 该配置避免你的站点遭受某些 CSRF 攻击。如果使用了通配符，你必须实现自定义的 Host HTTP 头，或者确保你不会很容易地遭受此种攻击。
    ALLOWED_HOSTS = [".bookhub.com.cn"]

    # Database
    # https://docs.djangoproject.com/en/4.2/ref/settings/#databases

    DATABASES = {
        "default": {
            "ENGINE": 'django.db.backends.postgresql',
            "NAME": cf.get(Django_ENV, 'Django_DB_NAME'),
            "USER": cf.get(Django_ENV, 'Django_DB_USER'),
            "PASSWORD": cf.get(Django_ENV, 'Django_DB_PASSWORD'),
            "HOST": cf.get(Django_ENV, 'Django_DB_HOST'),
            "PORT": cf.getint(Django_ENV, 'Django_DB_PORT'),
        }
    }

    INSTALLED_APPS += [
        'gunicorn',  # 部署用
    ]
else:
    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

    DEBUG = True

    SECRET_KEY = cf.get(Django_ENV, 'Django_SECRET_KEY')

    ALLOWED_HOSTS = ["*"]

    DATABASES = {
        # "default": {
        #     "ENGINE": "django.db.backends.sqlite3",
        #     "NAME": BASE_DIR / "db.sqlite3",
        # }
        "default": {
            "ENGINE": 'django.db.backends.postgresql',
            "NAME": cf.get(Django_ENV, 'Django_DB_NAME'),
            "USER": cf.get(Django_ENV, 'Django_DB_USER'),
            "PASSWORD": cf.get(Django_ENV, 'Django_DB_PASSWORD'),
            "HOST": cf.get(Django_ENV, 'Django_DB_HOST'),
            "PORT": cf.getint(Django_ENV, 'Django_DB_PORT'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

# 登陆url和登陆后跳转url
LOGIN_URL = '/api-auth/login/'
LOGIN_REDIRECT_URL = '/api-auth/api-router/'


# session设置
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # 引擎（默认）
SESSION_COOKIE_NAME = "sessionid"  # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
SESSION_COOKIE_PATH = "/"  # Session的cookie保存的路径（默认）
SESSION_COOKIE_DOMAIN = None  # Session的cookie保存的域名（默认）
SESSION_COOKIE_SECURE = False  # 是否Https传输cookie（默认）
SESSION_COOKIE_HTTPONLY = True  # 是否Session的cookie只支持http传输（默认）
SESSION_COOKIE_AGE = 1209600  # Session的cookie失效日期（2周）（默认）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 是否关闭浏览器使得Session过期（默认）
SESSION_SAVE_EVERY_REQUEST = False  # 是否每次请求都保存Session，默认修改之后才保存（默认）
SESSION_CACHE_ALIAS = "default"  # 指定session使用的缓存配置

# csrf设置
CSRF_COOKIE_AGE = None  # CSRF cookie 的寿命，以秒为单位。
CSRF_COOKIE_DOMAIN = None  # 设置 CSRF cookie 时要使用的域
CSRF_COOKIE_HTTPONLY = False  # 是否对 CSRF cookie 使用 HttpOnly 标志
CSRF_COOKIE_NAME = "csrftoken"  # 用于 CSRF 认证令牌的 cookie 的名称
CSRF_COOKIE_PATH = "/"  # 在 CSRF cookie 上设置的路径
CSRF_COOKIE_SAMESITE = "Lax"  # CSRF cookie 上 SameSite 标志的值。该标志可防止在跨站点请求中发送 cookie。
CSRF_COOKIE_SECURE = False  # 是否为 CSRF cookie 使用安全 cookie
CSRF_USE_SESSIONS = False  # 是否将 CSRF 标记存储在用户的会话中，而不是 cookie 中
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'  # 当传入的请求被 CSRF 保护 拒绝时，要使用的视图函数的点分隔路径
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'  # 用于 CSRF 认证的请求头的名称。
CSRF_TRUSTED_ORIGINS = []  # 不安全请求的可信来源列表

# 缓存设置,执行创建表命令python manage.py createcachetable
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache',
    }
}
# CACHES = {
#     # 默认存储信息: 存到 0 号库
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://192.168.0.100:6379/0",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }

# 日志设置
# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#         },
#     },
#     "root": {
#         "handlers": ["console"],
#         "level": "WARNING",
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console"],
#             "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
#             "propagate": False,
#         },
#     },
# }

# 错误日志管理系统
sentry_sdk.init(
    dsn="https://5d4f9be8c3604527af964e7cdbca733f@o4503963655667712.ingest.sentry.io/4505156966350848",
    integrations=[
        DjangoIntegration(
            # 如何命名出现在 Sentry 性能监控中的事务。
            # "/myproject/myview/<foo>"如果你设置transaction_style="url".
            # "myproject.myview"如果你设置transaction_style="endpoint".
            # 默认值为"endpoint"。
            transaction_style='url',
            # 创建跨度并跟踪 Django 项目中所有中间件的性能。设置False为禁用。
            middleware_spans=True,
            # 在您的 Django 项目中创建跨度并跟踪所有Django 信号接收器函数的性能。设置False为禁用。
            signals_spans=True,
            # 创建跨度并跟踪对已配置缓存的所有读取操作的性能。跨度还包括缓存访问是命中还是未命中的信息。设置False为禁用。
            cache_spans=True,
        ),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

# 默认电子邮件地址，用于网站管理员的各种自动通信。这不包括发送到ADMINS和MANAGERS的错误信息
DEFAULT_FROM_EMAIL = 'heyares@163.com'

ADMINS = [
    ("daibeisi", "heyares@163.com"),
]

HAYSTACK_CONNECTIONS = {
    'default': {
        # 指定了Django HAYSTACK要使用的搜索引擎，whoosh_backend_cn就是我们修改的文件
        'ENGINE': 'DjangoProject.whoosh_cn_backend.WhooshEngine',
        # 指定搜索文件存放的位置
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
# 指定搜索结果分页方式为每页10条记录
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
# 指定实时更新索引，当有数据改变时，自动更新索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "zh-hans"  # 语言格式

TIME_ZONE = "Asia/Shanghai"  # 设置时区

USE_I18N = True  # 是否使用国际化 (i18n) 功能
# LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]  # 设置以指定 Django 应在何处查找翻译文件

USE_L10N = False  # 用于决定是否开启数据本地化。如果此设置为True，例如Django将使用当前语言环境的格式显示数字和日期。

USE_TZ = False  # 指定是否使用指定的时区(TIME_ZONE)的时间

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# 静态文件设置,执行创建表命令python manage.py collectstatic
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "file/static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

MEDIA_URL = "/media/"  # 上传文件url前缀
MEDIA_ROOT = os.path.join(BASE_DIR, "file/media")  # 上传的文件路径

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
