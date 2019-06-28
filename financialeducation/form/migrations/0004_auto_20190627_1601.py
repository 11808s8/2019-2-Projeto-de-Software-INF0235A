# Generated by Django 2.2.1 on 2019-06-27 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_formindexpage_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formindexpage',
            name='categories',
        ),
        migrations.AddField(
            model_name='formindexpage',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='form.Category'),
        ),
    ]
