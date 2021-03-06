# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Punch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('team_id', models.CharField(db_index=True, max_length=255)),
                ('team_domain', models.CharField(db_index=True, max_length=255)),
                ('channel_id', models.CharField(db_index=True, max_length=255)),
                ('channel_name', models.CharField(db_index=True, max_length=255)),
                ('user_id', models.CharField(db_index=True, max_length=255)),
                ('user_name', models.CharField(db_index=True, max_length=255)),
                ('command', models.CharField(db_index=True, max_length=255)),
                ('text', models.CharField(db_index=True, max_length=255)),
                ('response_url', models.CharField(max_length=255)),
                ('punch_type', models.CharField(db_index=True, default='list', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
    ]
