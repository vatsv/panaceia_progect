# Generated by Django 3.1.3 on 2020-12-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0041_auto_20201216_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermain',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='usermain',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=20, verbose_name='WhatsApp'),
        ),
    ]