# Generated by Django 3.1.4 on 2021-01-22 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_auto_20210121_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='status',
            field=models.CharField(blank=True, choices=[('new', 'Новая'), ('work', 'В работе'), ('success', 'Выполнено'), ('reject', 'Отказ')], max_length=11, null=True, verbose_name='Статус'),
        ),
    ]
