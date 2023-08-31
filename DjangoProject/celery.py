# -*- coding:utf-8 -*-
import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject.settings.production")  # 设置django环境

app = Celery('django_celery')

app.config_from_object('django.conf:settings', namespace='CELERY')  # 使用CELERY_ 作为前缀，在settings中写配置

app.autodiscover_tasks()  # 发现任务文件每个app下的task.py
