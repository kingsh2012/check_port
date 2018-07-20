# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import *


class instance_admin(admin.ModelAdmin):
    list_display = ('server_name', 'host', 'port', 'status', 'env_flag')
    search_fields = ('server_name', 'host', 'port', 'status', 'env_flag')


admin.site.register(instance, instance_admin)
