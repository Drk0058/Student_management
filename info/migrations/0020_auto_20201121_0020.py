# Generated by Django 3.1.3 on 2020-11-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0019_auto_20201121_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='room',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
