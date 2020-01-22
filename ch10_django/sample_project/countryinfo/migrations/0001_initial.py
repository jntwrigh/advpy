# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-17 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=20)),
                ('capital', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]