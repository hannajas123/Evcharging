# Generated by Django 3.2.18 on 2023-09-18 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Evapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slots',
            name='place',
        ),
        migrations.RemoveField(
            model_name='slots',
            name='slotno',
        ),
    ]
