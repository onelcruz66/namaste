# Generated by Django 5.0.4 on 2024-05-31 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namaste_app', '0003_alter_messagerequest_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvedappointments',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='messagerequest',
            name='last_name',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='requestappointment',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]