# Generated by Django 3.1 on 2020-08-22 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targets', '0011_auto_20200821_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='target_image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
