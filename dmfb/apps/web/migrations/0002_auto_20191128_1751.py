# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-11-28 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='项目名')),
                ('repo', models.URLField(verbose_name='git仓库地址')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectEnv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('env', models.IntegerField(choices=[(1, '测试'), (2, '正式')], verbose_name='环境')),
                ('path', models.CharField(max_length=128, verbose_name='线上部署路径')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Project', verbose_name='项目')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=32, verbose_name='主机名')),
            ],
        ),
        migrations.AddField(
            model_name='projectenv',
            name='servers',
            field=models.ManyToManyField(to='web.Server', verbose_name='服务器'),
        ),
    ]
