# Generated by Django 2.2.10 on 2021-09-02 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20210901_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='bim',
            field=models.BooleanField(default=False),
        ),
    ]
