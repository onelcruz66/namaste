# Generated by Django 5.0.4 on 2024-06-12 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namaste_app', '0006_signeddocument_signature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signeddocument',
            name='document_signed',
        ),
        migrations.RemoveField(
            model_name='signeddocument',
            name='name',
        ),
        migrations.AddField(
            model_name='signeddocument',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='signeddocument',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='signeddocument',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='signeddocument',
            name='phone_number',
            field=models.CharField(default='', max_length=50),
        ),
    ]
