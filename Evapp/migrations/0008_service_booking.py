# Generated by Django 3.2.18 on 2023-10-12 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Evapp', '0007_auto_20230919_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_service', models.CharField(default='', max_length=100)),
                ('status', models.CharField(default='', max_length=100)),
                ('SERVICE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evapp.services')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evapp.users')),
                ('WORKER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Evapp.workers')),
            ],
        ),
    ]
