# Generated by Django 5.0.4 on 2024-07-30 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namaste_app', '0021_alter_requestappointment_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='requestappointment',
            name='time',
        ),
    ]