# Generated by Django 2.1.4 on 2018-12-15 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_info',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='employee_info',
            name='description',
        ),
        migrations.RemoveField(
            model_name='employee_info',
            name='totallCost',
        ),
    ]