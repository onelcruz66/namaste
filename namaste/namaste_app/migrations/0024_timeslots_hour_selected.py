# Generated by Django 5.0.4 on 2024-08-01 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namaste_app', '0023_timeslots_delete_appointments'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslots',
            name='hour_selected',
            field=models.CharField(choices=[('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('1:00', '1:00'), ('2:00', '2:00'), ('3:00', '3:00'), ('4:00', '4:00'), ('5:00', '5:00')], default='', max_length=50),
        ),
    ]
