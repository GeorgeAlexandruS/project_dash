# Generated by Django 2.2.10 on 2021-09-01 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='number',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
