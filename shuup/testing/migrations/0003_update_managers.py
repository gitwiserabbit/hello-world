# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-22 23:00
from __future__ import unicode_literals

from django.db import migrations
import shuup.utils.migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_testing', '0002_add_filters'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='carrierwithcheckoutphase',
            managers=(shuup.utils.migrations.get_managers_for_migration()),
        ),
        migrations.AlterModelManagers(
            name='paymentwithcheckoutphase',
            managers=(shuup.utils.migrations.get_managers_for_migration()),
        ),
        migrations.AlterModelManagers(
            name='pseudopaymentprocessor',
            managers=(shuup.utils.migrations.get_managers_for_migration()),
        ),
    ]