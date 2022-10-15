from authApp.models.historiaClinica import HistoriaClinica
from rest_framework import serializers

class HistoriaClinicaSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoriaClinica
        fields = '__all__'