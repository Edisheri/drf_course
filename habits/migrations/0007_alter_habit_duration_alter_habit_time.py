# Generated by Django 5.0.3 on 2024-03-12 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0006_alter_habit_options_remove_habit_start_point_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='duration',
            field=models.DurationField(default='00:00:00', verbose_name='Выполнять чч:мм:сс'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(default=datetime.time(12, 48, 14, 915801), verbose_name='Во сколько?'),
        ),
    ]
