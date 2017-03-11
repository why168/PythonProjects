from django.contrib import admin

# Register your models here.

from .models import Teacher
from .models import CourseOrg
from .models import CityDict


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)


class CourseOrgAdmin(admin.ModelAdmin):
    pass


admin.site.register(CourseOrg, CourseOrgAdmin)


class CityDictAdmin(admin.ModelAdmin):
    pass


admin.site.register(CityDict, CityDictAdmin)