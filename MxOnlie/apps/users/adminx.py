# -*- coding:utf-8 -*-
__author__ = 'Edwin.Wu'
__date__ = '2017/3/10 18:37'

import xadmin

from .models import EmailVerityRecord


class EmailVerityRecordAdmin(object):
    pass


xadmin.site.register(EmailVerityRecord, EmailVerityRecordAdmin)

