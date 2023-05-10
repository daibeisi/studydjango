import time
from django.utils.deprecation import MiddlewareMixin  # 中间件必须继承这个类
import logging

logger = logging.getLogger(__name__)


class TestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        logger.info("测试中间件的process_request()运行，请求URL是：{}".format(request.path_info))
        # 存放请求过来时的时间
        request.init_time = time.time()

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        logger.info("测试中间件的process_view()运行, 请求URL是：{}".format(request.path_info))

    def process_exception(self, request, exception):
        logger.info("测试中间件的process_exception()运行, 请求URL是：{}".format(request.path_info))

    def process_response(self, request, response):
        logger.info("测试中间件的process_response()运行, 请求URL是：{}, "
                    "状态短语：{}".format(request.path_info, response.reason_phrase))
        try:
            # 耗时
            localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # 请求路径
            path = request.path
            # 请求方式
            method = request.method
            # 响应状态码
            status_code = response.status_code
            message = '%s %s %s %s' % (localtime, path, method, status_code)
            logger.info(message)
        except Exception as e:
            logger.critical('系统错误')
        return response

    def process_template_response(self, request, response):
        logger.info("测试中间件的process_template_response()运行, 请求URL是：{}".format(request.path_info))
        return response
