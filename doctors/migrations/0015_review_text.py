# Generated by Django 3.1.4 on 2021-02-10 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0014_auto_20210210_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='text',
            field=models.TextField(blank=True, max_length=3000, verbose_name='Текст'),
        ),
    ]
