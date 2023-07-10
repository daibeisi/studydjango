#!/bin/bash


export PYTHONUNBUFFERED=1
export VIRTUAL_ENV=/home/django/venv
export PATH="/home/django/venv/bin:$PATH"

export OSS_ACCESS_KEY_ID=""
export OSS_ACCESS_KEY_SECRET=""
export OSS_BUCKET_NAME=""
export OSS_ENDPOINT="http://oss-cn-hangzhou.aliyuncs.com"
export OSS_EXPIRE_TIME=94608000

gunicorn -c gunicorn.conf.py