from django.contrib import admin
from .models.user import User
from .models.medico import Medico
admin.site.register(User)
admin.site.register(Medico)
