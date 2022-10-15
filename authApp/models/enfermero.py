from django.db import models
from .user import User

class Enfermero(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='enfermero', on_delete=models.CASCADE)
    area = models.CharField('area', max_length = 30)
    
    