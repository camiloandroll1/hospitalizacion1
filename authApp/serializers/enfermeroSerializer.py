from authApp.models.user import User
from authApp.models.enfermero import Enfermero
from rest_framework import serializers

class EnfermeroSerializer(serializers.ModelSerializer):
    area = serializers.CharField(max_length = 30)
    role = serializers.IntegerField(default=2)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'nombre', 'apellido','celular','direccion','email','role','area']
   
   
   
    def create(self, validated_data):
        areaData = validated_data.pop('area')
        validated_data['role'] = 2
        userInstance = User.objects.create(**validated_data)
        Enfermero.objects.create(user=userInstance, area=areaData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        enfermero = Enfermero.objects.get(user=obj.id)       
        
        return {
                    'id': user.id,
                    'username': user.username,
                    'nombre': user.nombre,
                    'apellido': user.apellido,
                    'celular': user.celular,
                    'direccion': user.direccion,
                    'email': user.email,
                    'role': user.role,
                    'area': enfermero.area
                    
                }