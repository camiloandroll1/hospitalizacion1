from authApp.models.user import User
from authApp.models.familiar import Familiar
from rest_framework import serializers

class FamiliarSerializer(serializers.ModelSerializer):
    parentesco = serializers.CharField(max_length = 30)
    role = serializers.IntegerField(default=3)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'nombre', 'apellido','celular','direccion','email','role','parentesco']
   
   
   
    def create(self, validated_data):
        parentescoData = validated_data.pop('parentesco')
        validated_data['role'] = 3
        userInstance = User.objects.create(**validated_data)
        Familiar.objects.create(user=userInstance, parentesco=parentescoData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        familiar = Familiar.objects.get(user=obj.id)       
        
        return {
                    'id': user.id,
                    'username': user.username,
                    'nombre': user.nombre,
                    'apellido': user.apellido,
                    'celular': user.celular,
                    'direccion': user.direccion,
                    'email': user.email,
                    'role': user.role,
                    'parentesco': familiar.parentesco
                    
                }