# Generated by Django 5.0.4 on 2024-06-17 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namaste_app', '0014_clientlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientlog',
            name='payment_type',
            field=models.CharField(choices=[('ATHMovil', 'ATHMovil'), ('Cash', 'Cash'), ('Credit', 'Credit'), ('Debit', 'Debit')], default='', max_length=50),
        ),
    ]
