# Generated by Django 2.2.10 on 2021-09-01 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0009_auto_20210901_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='pm',
        ),
        migrations.AddField(
            model_name='project',
            name='pm',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='pm', to=settings.AUTH_USER_MODEL),
        ),
    ]
