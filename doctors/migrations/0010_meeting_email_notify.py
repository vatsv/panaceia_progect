# Generated by Django 3.1.4 on 2021-01-29 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0009_auto_20210129_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='email_notify',
            field=models.BooleanField(blank=True, default=0, verbose_name='Уведомление'),
        ),
    ]