# Generated by Django 5.0.4 on 2024-09-06 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('namaste_app', '0025_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestappointment',
            old_name='date',
            new_name='date_requested',
        ),
    ]