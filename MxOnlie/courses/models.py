# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'课程名称')
    desc = models.CharField(max_length=300, verbose_name=u'课程描述')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(max_length=2, choices=(('cj', u'初级'), ('zj', u'中级'), ('gj', u'高级')))
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长(分钟数)')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name=u'封面图', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name















