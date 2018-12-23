from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin

from .models import Employee


class GlobalSettings(object):
    site_title = "维修后台管理系统"
    site_footer = "维修管理"


class EmployeeAdmin(object):
    list_display = ['user', 'name', 'birthday', 'gender', 'units','moblie','email','image']
    search_fields = ['user', 'name', 'birthday', 'gender', 'units','moblie','email','image']
    list_filter = ['user', 'name', 'birthday', 'gender', 'units','moblie','email','image']
    model_icon = 'fa fa-university'


xadmin.site.register(Employee, EmployeeAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)