# -*- coding:utf-8 -*-
__author__ = 'Edwin.Wu'
__date__ = '2017/3/19 23:01'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=5)
    password = forms.CharField(required=True, min_length=5)