# Generated by Django 3.1.4 on 2021-12-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211201_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
