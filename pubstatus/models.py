#--*-coding:utf-8---*---
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class instance(models.Model):
    '''
    当instance实例的env_flag环境设置为custom自定义时，将不会nginx检测自动删除
    '''
    server_name = models.CharField(max_length=100, blank=True, null=True)
    host = models.CharField(max_length=45)
    port = models.IntegerField()
    UNKONWN, LIVE, DIE = 1, 2, 3
    STATUS_CHOICES = ((UNKONWN, '未知'),
                      (LIVE, '在线'),
                      (DIE, '离线'))
    status = models.IntegerField(choices=STATUS_CHOICES, default=UNKONWN)
    ONLINE, TEST, CUSTOM = "online", "test", "custom"
    ENV_CHOICES = ((ONLINE, '线上nginx'),
                      (TEST, '测试nginx'),
                      (CUSTOM, '自定义'))
    env_flag = models.CharField(max_length=10, choices=ENV_CHOICES, default=CUSTOM)
