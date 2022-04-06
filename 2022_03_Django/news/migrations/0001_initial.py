# Generated by Django 4.0.2 on 2022-03-04 07:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('n_no', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('n_title', models.CharField(max_length=1000)),
                ('n_content', models.TextField()),
                ('n_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 4, 16, 48, 31, 36961))),
                ('n_hit', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('c_no', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('c_pw', models.CharField(blank=True, max_length=10)),
                ('c_content', models.TextField()),
                ('c_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 4, 16, 48, 31, 36961), null=True)),
                ('c_spw', models.IntegerField(default='1234')),
                ('news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.news')),
            ],
        ),
    ]