# Generated by Django 3.2.3 on 2021-06-24 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chriswellschool', '0006_rename_select_course_registerstudent_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerstudent',
            name='course',
            field=models.CharField(max_length=300),
        ),
    ]
