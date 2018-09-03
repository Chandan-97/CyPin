# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-03 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CyPin_View', '0002_auto_20180903_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Returned_Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField(default=-1)),
                ('returned_date', models.DateTimeField(auto_now_add=True)),
                ('returned_quantity', models.IntegerField(default=0)),
                ('returned_by', models.CharField(default='N/A', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Returned_Items',
            },
        ),
        migrations.AlterModelOptions(
            name='issued_items',
            options={'verbose_name_plural': 'Issued_Items'},
        ),
    ]
