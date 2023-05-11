""" simpleui 配置

    simpleui 配置，配置相关参数供 settings.py 导入引用
"""

SIMPLEUI_DEFAULT_THEME = "simpleui.css"
SIMPLEUI_LOGO = "/static/logo.png"
# 隐藏首页的快捷操作和最近动作
# SIMPLEUI_HOME_INFO = False
# SIMPLEUI_HOME_QUICK = False
# SIMPLEUI_ANALYSIS = False
# SIMPLEUI_LOADING = True


# 修改左侧菜单首页设置
# SIMPLEUI_HOME_PAGE = "/check/dashboard/"
SIMPLEUI_HOME_TITLE = "首页"
SIMPLEUI_HOME_ICON = "fa fa-home"

# 设置右上角Home图标跳转链接，会以另外一个窗口打开
# SIMPLEUI_INDEX = 'https://www.baidu.com'

# 注意key名为菜单上实际显示的名字，不是模型或App名。
# SIMPLEUI_DEFAULT_ICON = False
# SIMPLEUI_ICON = {
#     '系统管理': 'fab fa-apple',
#     '员工管理': 'fas fa-user-tie'
# }

# SIMPLEUI_CONFIG = {
#     'system_keep': False,
#     'menu_display': ["文章管理", "投票管理", "点检管理", "配置管理", "权限管理"],
#     'dynamic': True,
#     'menus': [{
#         'name': '文章管理',
#         'icon': 'fas fa-book-open',
#         'url': '/admin/article/article/',
#     }, {
#         'name': '投票管理',
#         'icon': 'fas fa-list-check',
#         'url': '/admin/vote/vote/',
#     }, {
#         'name': '点检管理',
#         'icon': 'fas fa-list-check',
#         'url': '/admin/check/checkapply/',
#     }, {
#         'name': '配置管理',
#         'icon': 'fas fa-cog',
#         'models': [{
#             'name': '文章类别',
#             'icon': 'fas fa-book',
#             'url': '/admin/article/articlecategory/'
#         }, {
#             'name': '抽检品种',
#             'icon': 'fa fa-list',
#             'url': '/admin/check/checkcategory/'
#         }, {
#             'name': '区/县',
#             'icon': 'fa fa-list',
#             'url': '/admin/check/area/'
#         }, {
#             'name': '乡/镇/街道',
#             'icon': 'fa fa-list',
#             'url': '/admin/check/town/'
#         }]
#     }, {
#         'name': '权限管理',
#         'icon': 'fas fa-shield-alt',
#         'models': [{
#             'name': '用户',
#             'icon': 'fa fa-user',
#             'url': '/admin/auth/user/'
#         }, {
#             'name': '用户组',
#             'icon': 'fa fa-users-cog',
#             'url': '/admin/auth/group/'
#         }]
#     },]
# }
