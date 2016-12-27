# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=13)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification_name', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('board', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mothers_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(auto_now=True)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], max_length=10)),
                ('address', models.TextField()),
                ('joined_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='faculty',
            name='high_school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='high_school', to='home.Qualification'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='highest_qualification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='highest_qualification', to='home.Qualification'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='intermediate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intermediate', to='home.Qualification'),
        ),
    ]
