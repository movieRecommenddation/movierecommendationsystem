# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_movierating'),
    ]

    operations = [
        migrations.CreateModel(
            name='cinema_info',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=50)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
            options={
                'db_table': 'cinema_info',
            },
        ),
        migrations.CreateModel(
            name='movie_resource',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('resource', models.CharField(max_length=1000)),
                ('movie', models.ForeignKey(db_column='m_id', on_delete=django.db.models.deletion.CASCADE, to='comment.MovieInfo')),
            ],
            options={
                'db_table': 'movie_resource',
            },
        ),
        migrations.CreateModel(
            name='price_info',
            fields=[
                ('p_id', models.IntegerField(primary_key=True, serialize=False)),
                ('w_name', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('hall_name', models.CharField(max_length=20)),
                ('hall_type', models.CharField(max_length=20)),
                ('start_time', models.CharField(max_length=20)),
                ('end_time', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('cinema', models.ForeignKey(db_column='c_id', on_delete=django.db.models.deletion.CASCADE, to='comment.cinema_info')),
                ('movie', models.ForeignKey(db_column='m_id', on_delete=django.db.models.deletion.CASCADE, to='comment.MovieInfo')),
            ],
            options={
                'db_table': 'price_info',
            },
        ),
    ]