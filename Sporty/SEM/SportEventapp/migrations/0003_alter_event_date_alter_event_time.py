# Generated by Django 5.1.1 on 2024-12-07 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportEventapp', '0002_event_date_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(),
        ),
    ]