# -*- coding:utf-8 -*-
__author__ = 'Edwin.Wu'
__date__ = '2017/4/8 11:23'
from django import forms
from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']
