# Generated by Django 3.1.3 on 2020-11-20 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0016_auto_20201120_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='shortname',
        ),
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('Practical', 'Practical'), ('Theory', 'Theory')], default='Theory', max_length=50),
        ),
        migrations.AlterField(
            model_name='assigntime',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=15),
        ),
        migrations.AlterField(
            model_name='assigntime',
            name='period',
            field=models.CharField(choices=[('1st', '8:30 - 9:25'), ('2nd', '9:25 - 10:20'), ('3rd', '10:40 - 11:35'), ('4th', '11:35 - 12:30'), ('5th', '12:30 - 1:25'), ('6th', '1:45 - 2:40'), ('7th', '2:40 - 3:35'), ('8th', '3:35 - 4:30'), ('9th', '4:30 - 5:25'), ('10th', '5:25 - 6:20')], default='8:30 - 9:25', max_length=50),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date(2020, 11, 20)),
        ),
        migrations.AlterField(
            model_name='marks',
            name='name',
            field=models.CharField(choices=[('Mt 1', 'Mid-term 1'), ('Mt 2', 'Mid-term 2'), ('TA', 'Teacher Asessment'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='marksclass',
            name='name',
            field=models.CharField(choices=[('Mt 1', 'Mid-term 1'), ('Mt 2', 'Mid-term 2'), ('TA', 'Teacher Asessment'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50),
        ),
    ]
