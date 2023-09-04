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
SIMPLEUI_INDEX = '/'

# 注意key名为菜单上实际显示的名字，不是模型或App名。
SIMPLEUI_DEFAULT_ICON = False
SIMPLEUI_ICON = {
    '组织管理': 'fas fa-cog',
    '基础配置': 'fas fa-cog',
    '系统配置': 'fas fa-cog',
}

SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menu_display': ['组织管理', "基础配置", "系统配置", ],
    'dynamic': True,
    'menus': [{
        'name': '组织管理',
        'icon': 'fas fa-cog',
        'models': [{
            'name': '公司',
            'icon': 'fa fa-list',
            'url': '/admin/base/company/'
        }, {
            'name': '部门',
            'icon': 'fa fa-list',
            'url': '/admin/base/department/'
        }, {
            'name': '人员',
            'icon': 'fa fa-list',
            'url': '/admin/base/userinfo/'
        }]
    }, {
        'name': '基础配置',
        'icon': 'fas fa-cog',
        'models': [{
            'name': '地理',
            'icon': 'fas fa-cog',
            'models': [{
                'name': '国家',
                'icon': 'fa fa-list',
                'url': '/admin/base/country/'
            }, {
                'name': '省/自治区',
                'icon': 'fa fa-list',
                'url': '/admin/base/province/'
            }, {
                'name': '市',
                'icon': 'fa fa-list',
                'url': '/admin/base/city/'
            }, {
                'name': '区/县',
                'icon': 'fa fa-list',
                'url': '/admin/base/area/'
            }, {
                'name': '乡/镇/街道',
                'icon': 'fa fa-list',
                'url': '/admin/base/town/'
            }]
        }, {
            'name': '路由',
            'icon': 'fa fa-list',
            'url': '/admin/base/router/'
        }]
    }, {
        'name': '系统配置',
        'icon': 'fas fa-cog',
        'models': [
            {
                'name': '权限配置',
                'icon': 'fas fa-shield-alt',
                'models': [{
                    'name': '权限',
                    'icon': 'fa fa-users-cog',
                    'url': '/admin/auth/permission/'
                }, {
                    'name': '用户',
                    'icon': 'fa fa-user',
                    'url': '/admin/auth/user/'
                }, {
                    'name': '用户组',
                    'icon': 'fa fa-users-cog',
                    'url': '/admin/auth/group/'
                }, {
                    'name': '用户对象权限',
                    'icon': 'fa fa-users-cog',
                    'url': '/admin/guardian/userobjectpermission/'
                }, {
                    'name': '用户组对象权限',
                    'icon': 'fa fa-users-cog',
                    'url': '/admin/guardian/groupobjectpermission/'
                }]
            }, {
                'name': '令牌配置',
                'icon': 'fas fa-shield-alt',
                'models': [{
                    'name': '签发令牌',
                    'icon': 'fa fa-users-cog',
                    'url': '/admin/token_blacklist/outstandingtoken/'
                }, {
                    'name': '黑名单',
                    'icon': 'fa fa-user',
                    'url': '/admin/token_blacklist/blacklistedtoken/'
                }]
            }
        ]
    },]
}
