DjangoProject
----

This is django project repository for daibeisi.

Getting started with DjangoProject
-------------------------

+ DEV
  1. git clone git@github.com:daibeisi/studydjango.git
  2. git关闭跟踪文件修改提交 git update-index --assume-unchanged "DjangoProject.conf"
  3. 修改 DjangoProject.conf 配置文件中配置
  4. pip install -r requirements.txt
  5. python manage.py runserver 0:8000
  6. python manage.py createsuperuser
+ PROD
  1. git clone git@github.com:daibeisi/studydjango.git
  2. 将ssl证书放到 nginx/cert 目录下
  3. git关闭跟踪文件修改提交 git update-index --assume-unchanged "DjangoProject.conf"
  4. 修改 DjangoProject.conf 配置文件中配置
  5. docker-compose up -d --build
  6. 进入backend容器执行 python manage.py collectstatic && python manage.py createcachetable && python manage.py createsuperuser
```
NOTE: git打开跟踪文件修改提交 git update-index --no-assume-unchanged "DjangoProject.conf"
```

解决方案
-------------------------
# 导入导出
  django-import-export-celery
# restapi
  djangorestframework
# token认证
  djangorestframework-simplejwt
# 文件存储
  自定义文件存储系统，保存至阿里云OSS
# 后台样式
  django-simpleui
# 部署
  gunicorn + nginx + docker-compose
# 富文本编辑器
  django-ckeditor
# 自动报告错误和异常以及性能监控
  sentry
# 静态文件压缩
  django-compressor
+ 接口安全
  1. 请求身份是否合法？
  2. 请求参数是否篡改？
  3. 请求是否唯一？
  4. ip黑名单
  5. 接口限流
+ 数据库
  1. 多数据库（读写分离，主从复制，分库分表）
  2. 大表优化
  3. 字段优化（CharField确定长度， 尽量不用TextField）
  4. 使用索引
+ 缓存
  1. 缓存雪崩
  2. 缓存击穿
  3. 缓存穿透
+ 定时脚本
  1. 日志清理
+ 消息队列
+ 日志
  1. 日志可视化
+ 异步支持
  1. Uvicorn启动
  2. Daphne启动
+ 分布式
+ 分库
+ 性能优化
  指标：响应时间 最大并发连接数 代码的行数 函数调用次数 内存占用情况 CPU占比
  1. 使用django-debug-toolbar和django-silk来进行性能监测分析