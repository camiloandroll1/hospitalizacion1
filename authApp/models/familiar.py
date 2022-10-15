from django.db import models
from .user import User

class Familiar(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='familiar', on_delete=models.CASCADE)
    parentesco = models.CharField('parentesco', max_length = 30)
    
    