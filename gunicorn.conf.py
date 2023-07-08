import multiprocessing
from random import randint

wsgi_app = 'DjangoProject.wsgi:application'  # 模式中的 WSGI 应用程序路径$(MODULE_NAME):$(VARIABLE_NAME)。

# 日志
accesslog = "-"  # 访问日志文件，"-" 表示标准输出
access_log_format = '%(t)s %({x-real-ip}i)s %(l)s %(h)s %(l)s %(u)s %(l)s %(p)s "%(r)s" %(s)s %(L)s %(b)s "%(f)s" "%(' \
                    'a)s"'
errorlog = "/home/django/workspace/log/gunicorn_error.log"  # 错误日志文件
loglevel = 'info'  # 日志级别，这个日志级别指的是错误日志的级别，而访问日志的级别无法设置

# 进程命名
proc_name = 'gunicorn_server'  # 进程名

# SSL协议

# 安全
limit_request_line = 4094  # HTTP 请求行的最大大小（以字节为单位）。
limit_request_fields = 100  # 限制请求中 HTTP 标头字段的数量。
limit_request_field_size = 8190  # 限制 HTTP 请求标头字段允许的大小。

bind = "0.0.0.0:8000"  # 绑定的ip与端口
backlog = 2048  # 监听队列数量，64-2048
workers = multiprocessing.cpu_count() * 2 + 1  # 进程数
worker_class = 'gevent'  # 使用gevent模式，还可以使用sync 模式，默认的是sync模式
threads = multiprocessing.cpu_count() * 4  # 指定每个进程开启的线程数
worker_connections = 1000  # 同时客户端的最大数量。此设置仅影响 Eventlet 和 Gevent 工作线程类型。
max_requests = 2048  # 工作线程在重新启动之前将处理的最大请求数。
max_requests_jitter = randint(0, 200)  # 添加到max_requests设置的最大抖动。
timeout = 30  # 沉默超过这么多秒的工人将被杀死并重新启动。
graceful_timeout = 30  # 优雅工作线程重启超时。超时后（从收到重启信号开始）仍然活着的工作人员将被强制杀死。
keepalive = 60  # 等待保持活动连接上的请求的秒数。

# 服务器设置
# chdir = ''  # 加载应用程序之前，将目录更改为指定目录。
# raw_env = ['key=value']  # 在执行环境中设置环境变量。
worker_tmp_dir = '/dev/shm'  # /dev/shm is mapped to shared memory and should be used for gunicorn heartbeat
