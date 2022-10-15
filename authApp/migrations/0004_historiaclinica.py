# Generated by Django 4.1.2 on 2022-10-14 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_alter_enfermero_area_familiar'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('oximetria', models.CharField(max_length=20, verbose_name='oximetria')),
                ('frecuencia_resporatoria', models.CharField(max_length=20, verbose_name='frecuencia_respiratoria')),
                ('frecuencia_cardiaca', models.CharField(max_length=20, verbose_name='frecuencia_cardiaca')),
                ('temperatura', models.CharField(max_length=10, verbose_name='temperatura')),
                ('presion_arterial', models.CharField(max_length=10, verbose_name='presion_arterial')),
                ('glicemias', models.CharField(max_length=10, verbose_name='glicemias')),
                ('diagnostico', models.CharField(max_length=300, verbose_name='diagnostico')),
                ('cuidados', models.CharField(max_length=300, verbose_name='cuidados')),
            ],
        ),
    ]
