# Generated by Django 5.0.3 on 2024-03-11 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={'verbose_name': 'привычку', 'verbose_name_plural': 'привычек'},
        ),
        migrations.RemoveField(
            model_name='habit',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='time',
        ),
    ]
