# Generated by Django 4.2.2 on 2023-06-18 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructorDashboard', '0002_assignedassignment_assignment_assigned_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submittedassignment',
            name='assessment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
