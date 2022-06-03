# Generated by Django 2.2.10 on 2021-09-01 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20210901_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='contractor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='contractor', to='companies.Company'),
        ),
        migrations.AlterField(
            model_name='project',
            name='division',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='division', to='companies.Company'),
        ),
    ]