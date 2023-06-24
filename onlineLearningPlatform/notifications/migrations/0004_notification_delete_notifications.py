# Generated by Django 4.2.2 on 2023-06-22 15:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0010_alter_post_uploadtime_alter_reply_uploadtime'),
        ('instructorDashboard', '0006_alter_course_students'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0003_notifications_remove_forumnotifications_forum_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=False)),
                ('content', models.TextField()),
                ('timeStamp', models.DateTimeField(default=datetime.datetime(2023, 6, 22, 20, 36, 44, 816433))),
                ('assignment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='instructorDashboard.assignment')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructorDashboard.course')),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forums.forum')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forums.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Notifications',
        ),
    ]