# Generated by Django 5.0.4 on 2024-06-13 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namaste_app', '0011_alter_signeddocument_condition_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signeddocument',
            name='condition_names',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Condition Names'),
        ),
    ]
