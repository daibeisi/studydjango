import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


HAYSTACK_CONNECTIONS = {
    'default': {
        # 指定了Django HAYSTACK要使用的搜索引擎，whoosh_backend_cn就是我们修改的文件
        'ENGINE': 'DjangoProject.whoosh_cn_backend.WhooshEngine',
        # 指定搜索文件存放的位置
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
# 指定搜索结果分页方式为每页10条记录
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
# 指定实时更新索引，当有数据改变时，自动更新索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'