# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_name', models.CharField(blank=True, max_length=255, unique=True, verbose_name='Network Name')),
                ('network_file', models.FileField(upload_to='networks/', verbose_name='Network File')),
                ('network_type', models.CharField(choices=[('tlp', 'Tulip TLP'), ('ind', 'Industry Standard')], default='tlp', max_length=3, verbose_name='Network Type')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]