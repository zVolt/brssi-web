# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-15 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('type', models.CharField(choices=[('1', 'Scholarship'), ('2', 'Admission Form'), ('3', 'Other')], max_length=10)),
            ],
        ),
    ]
