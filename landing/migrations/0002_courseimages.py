# Generated by Django 3.0 on 2022-04-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('course_description', models.CharField(max_length=255)),
                ('Image_course_name', models.CharField(max_length=2083)),
            ],
        ),
    ]