from django.db import models
from .user import User
from .historiaClinica import HistoriaClinica

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='paciente', on_delete=models.CASCADE)
    medico = models.ForeignKey(User, related_name='medico_std', on_delete=models.CASCADE)
    familiar = models.ForeignKey(User, related_name='familiar_std', on_delete=models.CASCADE)
    enfermero = models.ForeignKey(User, related_name='enfermero_std', on_delete=models.CASCADE)
    historiaClinica = models.ForeignKey(HistoriaClinica, related_name='historiaClinica_std', on_delete=models.CASCADE)
    