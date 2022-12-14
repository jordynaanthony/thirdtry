# Generated by Django 4.0.2 on 2022-10-23 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog_number', models.SlugField(max_length=12)),
                ('name', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=4)),
                ('description', models.CharField(max_length=5000)),
                ('units', models.CharField(max_length=2)),
                ('class_capacity', models.IntegerField(default=0)),
                ('wait_list', models.IntegerField(default=0)),
                ('wait_cap', models.IntegerField(default=0)),
            ],
        ),
    ]