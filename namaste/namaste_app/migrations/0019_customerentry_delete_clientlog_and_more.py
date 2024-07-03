# Generated by Django 5.0.4 on 2024-06-21 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namaste_app', '0018_alter_signeddocument_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_seen', models.DateTimeField(auto_now_add=True, verbose_name='Date Seen')),
                ('treatment', models.CharField(blank=True, default='', max_length=100)),
                ('payment_type', models.CharField(choices=[('ATHMovil', 'ATHMovil'), ('Cash', 'Cash'), ('Credit', 'Credit'), ('Debit', 'Debit')], default='', max_length=50)),
                ('payment_amount', models.DecimalField(decimal_places=2, help_text='Price in dollars', max_digits=10)),
                ('comments', models.CharField(blank=True, default='', max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='ClientLog',
        ),
        migrations.RenameModel(
            old_name='SignedDocument',
            new_name='Customer',
        ),
        migrations.AddField(
            model_name='customerentry',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='namaste_app.customer'),
        ),
    ]