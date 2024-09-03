# Generated by Django 5.0.4 on 2024-07-29 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namaste_app', '0020_alter_customerentry_treatment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestappointment',
            name='service',
            field=models.CharField(choices=[('Gold Detox (6 Secciones)', 'Gold Detox (6 Secciones)'), ('Metaloterapia (6 Secciones)', 'Metaloterapia (6 Secciones)'), ('Maderoterapia (6 Secciones)', 'Maderoterapia (6 Secciones)'), ('Masaje Sueco', 'Masaje Sueco'), ('Post-Operatorio', 'Post-Operatorio'), ('Masaje Prenatal', 'Masaje Prenatal'), ('Masaje Profundo', 'Masaje Profundo'), ('Gold Detox', 'Gold Detox'), ('Vacuslim-48', 'Vacuslim-48'), ('Depilación', 'Depilación'), ('Maderoterapia', 'Maderoterapia'), ('Metaloterapia', 'Metaloterapia'), ('Drenaje Linfático', 'Drenaje Linfático'), ('Quiromasaje', 'Quiromasaje'), ('Copas Chinas', 'Copas Chinas'), ('Pistola De Masaje', 'Pistola De Masaje'), ('Maderoterapia Facial', 'Maderoterapia Facial'), ('Lipoláser', 'Lipoláser'), ('Vacumterapia', 'Vacumterapia'), ('LeBody', 'LeBody')], default='', max_length=50),
        ),
    ]