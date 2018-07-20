# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-07-20 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubstatus', '0004_instance_env_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='env_flag',
            field=models.CharField(choices=[('online', '\u7ebf\u4e0anginx'), ('test', '\u6d4b\u8bd5nginx'), ('custom', '\u81ea\u5b9a\u4e49')], default='custom', max_length=10),
        ),
    ]