# Generated by Django 3.1.4 on 2021-02-04 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0057_remove_userdoctor_specialty'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialtylist',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
