# -*- coding:utf-8 -*-
from organization.views import OrgView, AddUserAskView

__author__ = 'Edwin.Wu'
__date__ = '2017/4/8 20:41'

from django.conf.urls import url, include

urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask')

]
