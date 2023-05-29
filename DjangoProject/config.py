""" 项目配置文件读取

    项目配置文件读取，供 settings.py 导入引用
"""
import os
import configparser
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Reads the django service configuration file
cf = configparser.ConfigParser()
cf.read(os.path.join(BASE_DIR, 'DjangoProject.conf'))

