# Generated by Django 3.0.5 on 2020-04-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wafrahapp', '0002_auto_20200422_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='permissions',
        ),
        migrations.AddField(
            model_name='account',
            name='permissions',
            field=models.ManyToManyField(to='wafrahapp.Permission'),
        ),
    ]
