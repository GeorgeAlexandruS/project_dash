# Generated by Django 2.2.10 on 2021-09-01 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20210816_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='branch',
            new_name='division',
        ),
    ]