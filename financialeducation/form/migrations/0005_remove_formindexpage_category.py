# Generated by Django 2.2.2 on 2019-06-27 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_auto_20190627_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formindexpage',
            name='category',
        ),
    ]
