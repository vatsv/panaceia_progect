# Generated by Django 3.1.3 on 2020-12-15 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0035_auto_20201215_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='text',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='support',
            name='user_id',
            field=models.IntegerField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='support',
            name='user_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]