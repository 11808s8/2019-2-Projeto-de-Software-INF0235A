# Generated by Django 2.2.1 on 2019-06-27 15:49

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='formindexpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='form.Category'),
        ),
    ]
