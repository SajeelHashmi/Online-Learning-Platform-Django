# Generated by Django 4.2.2 on 2023-06-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0011_alter_post_uploadtime_alter_reply_uploadtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uploadTime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='reply',
            name='uploadTime',
            field=models.DateTimeField(),
        ),
    ]
