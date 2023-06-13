DjangoProject
----

This is django project repository for daibeisi.

Getting started with DjangoProject
-------------------------

+ DEV
  1. pip install -r requirements.txt
  2. python manage.py runserver 0:8000
+ PROD
  1. sudo docker-compose up -d --build

解决方案
-------------------------
# 导入导出
  django-import-export
# restapi
  djangorestframework
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