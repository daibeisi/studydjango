DjangoStudy
----

This is django-learning repository for daibeisi.

Getting started with DjangoStudy
-------------------------

+ DEV
  1. pip install -r requirements.txt
  2. python manage.py runserver 0:8000
+ PROD
  1. sudo docker-compose up -d --build

解决方案
-------------------------
+ 接口安全
  1. 请求身份是否合法？
  2. 请求参数是否篡改？
  3. 请求是否唯一？
  4. ip黑名单
  5. 接口限流
+ 数据库
  1. 多数据库
  2. 大表优化
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