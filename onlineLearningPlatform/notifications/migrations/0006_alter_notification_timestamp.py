# Generated by Django 4.2.2 on 2023-06-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_remove_notification_forum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='timeStamp',
            field=models.DateTimeField(),
        ),
    ]
