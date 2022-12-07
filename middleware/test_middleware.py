from django.utils.deprecation import MiddlewareMixin  # 中间件必须继承这个类


class TestMiddleware1(MiddlewareMixin):

    def process_request(self, request):
        print("测试中间件1的process_request()运行，请求URL是：", request.path_info)

    def process_response(self, request, response):
        print("测试中间件1的process_response()进行相应，状态短语：", response.reason_phrase)
        return response

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print("测试中间件1的process_view()运行")

    def process_exception(self, request, exception):
        print("测试中间件1的process_exception()运行")

    def process_template_response(self, request, response):
        print("测试中间件1的process_template_response()运行")
        return response


class TestMiddleware2(MiddlewareMixin):

    def process_request(self, request):
        print("测试中间件2的process_request()运行，请求URL是：", request.path_info)

    def process_response(self, request, response):
        print("测试中间件2的process_response()进行相应，状态短语：", response.reason_phrase)
        return response

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print("测试中间件2的process_view()运行")

    def process_exception(self, request, exception):
        print("测试中间件2的process_exception()运行")

    def process_template_response(self, request, response):
        print("测试中间件2的process_template_response()运行")
        return response
