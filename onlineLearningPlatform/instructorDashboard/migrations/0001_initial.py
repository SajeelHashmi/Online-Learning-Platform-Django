# Generated by Django 4.2.2 on 2023-06-17 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0003_student_delete_userprofile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='assignment_files')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubmittedAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment', models.TextField()),
                ('submission_file', models.FileField(upload_to='submission_files')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructorDashboard.assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.student')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='instructor_profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subject', models.CharField(max_length=100)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructorDashboard.instructor')),
                ('students', models.ManyToManyField(related_name='courses', to='signup.student')),
                ('tags', models.ManyToManyField(to='instructorDashboard.tag')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructorDashboard.course'),
        ),
    ]