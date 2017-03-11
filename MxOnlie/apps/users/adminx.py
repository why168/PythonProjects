# -*- coding:utf-8 -*-
__author__ = 'Edwin.Wu'
__date__ = '2017/3/10 18:37'

import xadmin

from xadmin import views
from .models import EmailVerityRecord, Banner


# 自定义主题设置,导入xadmin.views.BaseAdminView,再进行注册
class BassSetting(object):
    enable_themes = True
    use_bootswatch = True


# 设置头和尾,导入xadmin.views.CommAdminView,再进行注册
class GlobalSettings(object):
    site_title = '慕学后台管理系统'
    site_footer = '慕学在线网'
    menu_style = 'accordion'  # 菜单样式


class EmailVerityRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerityRecord, EmailVerityRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BassSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
