# Generated by Django 3.1.3 on 2020-12-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0027_auto_20201210_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdoctor',
            name='experienceText',
            field=models.CharField(blank=True, max_length=3000, verbose_name='Опыт работы'),
        ),
        migrations.AddField(
            model_name='userdoctor',
            name='experienceYears',
            field=models.CharField(blank=True, max_length=2, verbose_name='Стаж'),
        ),
    ]