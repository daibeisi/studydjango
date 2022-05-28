# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /Django
COPY . /Django/
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
RUN ln -s /Django/sources.list /etc/apt/
RUN apt-get update -y
RUN apt-get install nginx -y
RUN python -m pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
RUN ln -s /Django/StudyDjango_nginx.conf /etc/nginx/sites-enabled
