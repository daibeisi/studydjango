# syntax=docker/dockerfile:1
FROM python:3

# 设置Python解释器不生成字节码pyc文件
# ENV PYTHONDONTWRITEBYTECODE=1

# 相当于设置 python 命令行的 -u 选项
# 不缓冲stdin、stdout和stderr，默认是缓冲的。
ENV PYTHONUNBUFFERED=1

WORKDIR /Django
COPY . /Django/

# docker build过程中执行命令
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak \
    && ln -s /Django/sources.list /etc/apt/ \
    && apt-get -y update \
    && apt-get -y install nginx \
    && python -m pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/ \
    && pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ \
    && ln -s /Django/DjangoServer.conf /etc/nginx/sites-enabled
# 声明端口
#EXPOSE 8000
# 设置默认执行的命令，docker run 时运行
# CMD XXX
#LABEL org.opencontainers.image.authors="daibeisi"
