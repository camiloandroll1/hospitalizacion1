from rest_framework import serializers
from authApp.models.user import User
from authApp.models.medico import Medico


class MedicoSerializer(serializers.ModelSerializer):
    especialidad = serializers.CharField(max_length = 30)
    role = serializers.IntegerField(default=1)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'nombre', 'apellido','celular','direccion','email','role','especialidad']
    
    def create(self, validated_data):
        especialidadData = validated_data.pop('especialidad')
        validated_data['role'] = 1
        userInstance = User.objects.create(**validated_data)
        Medico.objects.create(user=userInstance, especialidad=especialidadData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        medico = Medico.objects.get(user=obj.id)
        
        return {
                    'id': user.id,
                    'username': user.username,
                    'nombre': user.name,
                    'apellido': user.apellido,
                    'celular': user.celular,
                    'direccion': user.direccion,
                    'email': user.email,
                    'role': user.role,
                    'especialidad': medico.especialidad
                    
                }