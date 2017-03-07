# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


# Create your models here.

class UserMessage(models.Model):
    object_id = models.CharField(max_length=50, default="", primary_key=True, verbose_name=u'主键')
    name = models.CharField(max_length=20, default="", verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"联系地址")
    message = models.CharField(max_length=500, verbose_name=u"留言信息")

    def __str__(self):
        return '(UserMessage: %s, %s, %s, %s, %s)' % (self.object_id, self.name, self.email, self.address, self.message)

    class Meta:
        verbose_name = u"用户留言信息"
        verbose_name_plural = verbose_name  # 复数信息
        db_table = "user_message"  # 表名字
        ordering = ['-object_id']  # 降序排列
        # ordering = ['object_id']  # 升序排列
