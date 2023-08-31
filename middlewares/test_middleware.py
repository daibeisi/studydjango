from datetime import datetime
from django.utils.deprecation import MiddlewareMixin  # 中间件必须继承这个类
import logging

logger = logging.getLogger(__name__)


class TestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.init_time = datetime.now()

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        logger.info("测试中间件的process_view()运行, 请求URL是：{}".format(request.path_info))

    def process_exception(self, request, exception):
        logger.info("测试中间件的process_exception()运行, 请求URL是：{}".format(request.path_info))

    def process_response(self, request, response):
        localtime = datetime.now()

    def process_template_response(self, request, response):
        logger.info("测试中间件的process_template_response()运行, 请求URL是：{}".format(request.path_info))
        return response