# TODO:因为设置文件包含敏感信息，应该尽一切努力限制对它的访问。例如，更改其文件权限，以便只有您和您的 Web 服务器的用户可以读取它。
"""
Django settings for StudyDjango project.
Generated by 'django-admin startproject' using Django 3.2.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent  # 获取项目的根路径

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

"""关键配置"""
CURRENT_ENV = os.environ.get('CURRENT_ENV', "dev")
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if CURRENT_ENV == 'prod' else True
# 该配置避免你的站点遭受某些 CSRF 攻击。如果使用了通配符，你必须实现自定义的 Host HTTP 头，或者确保你不会很容易地遭受此种攻击。
ALLOWED_HOSTS = ['*'] if CURRENT_ENV == 'prod' else ['127.0.0.1']
# 默认电子邮件地址，用于网站管理员的各种自动通信。这不包括发送到ADMINS和MANAGERS的错误信息
DEFAULT_FROM_EMAIL = 'webmaster@example.com'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
#         'PORT': os.environ.get('DB_PORT', 5432),
#     }
# }

# Application definition
# 新建app需要加到这里
INSTALLED_APPS = [
    # 默认应用，为了方便大多数项目，如果不需要某个或某些应用，你可以在运行 migrate 前毫无顾虑注释或者删除掉它们
    'django.contrib.admin',  # 管理员站点
    'django.contrib.auth',  # 认证授权系统
    'django.contrib.contenttypes',  # 内容类型框架
    'django.contrib.sessions',  # 会话框架
    'django.contrib.messages',  # 消息框架
    'django.contrib.staticfiles',  # 管理静态文件的框架
    # 注册引入应用
    'haystack',
    'ckeditor',
    'ckeditor_uploader',
    # 注册自定义应用
    'Apps.base',
    # 'Apps.comments',
    # 'Apps.company'
]

# TODO:使用自定义用户模型，完善user应用程序
# 设置认证系统中使用的用户模型, 例如这里指定为使用user应用程序中User模型
# AUTH_USER_MODEL = "blog.BlogUser"

# 中间件，响应前自动处理
MIDDLEWARE = [
    'middleware.test_middleware.TestMiddleware1',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.test_middleware.TestMiddleware2'
]

# 指项目文件下同名文件夹下的urls，项目改名字这里也要改
ROOT_URLCONF = 'StudyDjango.urls'

# 指定模板路径 BASE_DIR是项目根路径，有别的模板也要加进来
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 添加如下配置，即可不用每个模板中添加{% load static %}
            'builtins': [
                'django.templatetags.static'
            ],
        },
    },
]

WSGI_APPLICATION = 'StudyDjango.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  # 语言格式

TIME_ZONE = 'Asia/Shanghai'  # 设置时区

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# 静态文件的路由（url）地址
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = '/static/'

MEDIA_URL = '/media/'  # 上传文件url前缀
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 上传的文件路径

# 登陆url和登陆后跳转url
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/index/'

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

# ckeditor设置
CKEDITOR_UPLOAD_PATH = 'ckeditor/'  # 设置富文本编辑器的上传文件的相对路径
CKEDITOR_IMAGE_BACKEND = 'pillow'  # 设置图片处理的引擎为pillow，用于生成图片缩略图，在编辑器里浏览上传的图片
CKEDITOR_BROWSE_SHOW_DIRS = True  # 在编辑器浏览上传的图片时，图片会以路径分组、以日期排序
# 限制用户浏览图片文件的权限、只能浏览自己上传的图片、图片会传到以用户名命名的文件夹下，但超级用户可以查看所有图片
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_CONFIGS = {
    # 配置名是default时，django-ckeditor默认使用这个设置
    'default': {
        'toolbar': (
            ['div', 'Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', 'Scayt'],
            ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat'],
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks', '-', 'About', 'pbckcode'],
        ),
    },
    # 设置另一个django-ckeditor配置
    'test': {
        # 使用简体中文
        'language': 'zh-cn',
        # 设置富文本编辑器的宽度和高度
        'width': '660px',
        'height': '200px',
        # 设置工具栏为自定义，名字为Custom
        'toolbar': 'Custom',
        # 添加富文本编辑器的工具栏按钮
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList'],
            ['Image', 'Link', 'Unlink'],
            ['Maximize']
        ]
    },
}

HAYSTACK_CONNECTIONS = {
    'default': {
        # 指定了Django HAYSTACK要使用的搜索引擎，whoosh_backend_cn就是我们修改的文件
        'ENGINE': 'StudyDjango.whoosh_backend_cn.WhooshEngine',
        # 指定搜索文件存放的位置
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
# 指定搜索结果分页方式为每页6条记录
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 6
# 指定实时更新索引，当有数据改变时，自动更新索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# 缓存设置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache',
    }
}
# 执行创建表命令python manage.py createcachetable

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
