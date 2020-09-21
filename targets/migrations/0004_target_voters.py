# Generated by Django 3.1 on 2020-08-09 16:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('targets', '0003_remove_target_voters'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='voters',
            field=models.ManyToManyField(related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
