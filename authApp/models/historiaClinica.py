from django.db import models

class HistoriaClinica(models.Model):
    id = models.AutoField(primary_key=True)
    oximetria = models.CharField('oximetria', max_length = 20)
    frecuencia_resporatoria = models.CharField('frecuencia_respiratoria', max_length = 20)
    frecuencia_cardiaca = models.CharField('frecuencia_cardiaca', max_length = 20)
    temperatura = models.CharField('temperatura', max_length = 10)
    presion_arterial = models.CharField('presion_arterial', max_length = 10)
    glicemias = models.CharField('glicemias', max_length = 10)
    diagnostico = models.CharField('diagnostico', max_length = 300)
    cuidados = models.CharField('cuidados', max_length = 300)
