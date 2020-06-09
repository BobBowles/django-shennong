# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Herb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('chinese', models.CharField(max_length=20)),
                ('pinyin', models.CharField(max_length=50)),
                ('latin', models.CharField(max_length=200)),
                ('english', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('herb', models.ForeignKey(to='shennong.Herb', on_delete=models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('chinese', models.CharField(max_length=20)),
                ('pinyin', models.CharField(max_length=50)),
                ('english', models.CharField(max_length=200)),
                ('ingredients', models.ManyToManyField(to='shennong.Herb', through='shennong.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(to='shennong.Recipe', on_delete=models.CASCADE),
        ),
    ]
