# Generated by Django 3.1.4 on 2020-12-22 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0051_userdoctor_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
