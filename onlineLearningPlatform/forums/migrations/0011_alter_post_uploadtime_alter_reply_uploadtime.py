# Generated by Django 4.2.2 on 2023-06-23 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0010_alter_post_uploadtime_alter_reply_uploadtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uploadTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 15, 36, 59, 88744)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='uploadTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 15, 36, 59, 88744)),
        ),
    ]