# Generated by Django 3.1 on 2020-08-09 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('targets', '0002_auto_20200808_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='target',
            name='voters',
        ),
    ]