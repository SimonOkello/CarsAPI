# Generated by Django 3.2.7 on 2022-03-01 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20220301_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trim',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
