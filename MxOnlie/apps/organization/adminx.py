# -*- coding:utf-8 -*-
__author__ = 'Edwin.Wu'
__date__ = '2017/3/11 00:19'

import xadmin

from .models import Teacher
from .models import CourseOrg
from .models import CityDict


class TeacherAdmin(object):
    pass


xadmin.site.register(Teacher, TeacherAdmin)


class CourseOrgAdmin(object):
    pass


xadmin.site.register(CourseOrg, CourseOrgAdmin)


class CityDictAdmin(object):
    pass


xadmin.site.register(CityDict, CityDictAdmin)