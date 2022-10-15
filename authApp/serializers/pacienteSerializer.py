from authApp.models.user import User
from authApp.models.paciente import Paciente
from authApp.models.medico import Medico
from authApp.models.enfermero import Enfermero
from authApp.models.familiar import Familiar
from authApp.models.historiaClinica import HistoriaClinica
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    medico_id = serializers.IntegerField()
    enfermero_id = serializers.IntegerField()
    familiar_id = serializers.IntegerField()
    historiaClinica_id = serializers.IntegerField()
    role = serializers.IntegerField(default=4)

    class Meta:
        model = HistoriaClinica
        model = User
        fields = ['id', 'username', 'password', 'nombre', 'apellido', 'celular', 'direccion', 'email', 'role', 'medico_id','enfermero_id','familiar_id','historiaClinica_id']

    def create(self, validated_data):
        medicoIdData = validated_data.pop('medico_id')
        enfermeroIdData = validated_data.pop('enfermero_id')
        familiarIdData = validated_data.pop('familiar_id')
        historiaClinicaIdData = validated_data.pop('historiaClinica_id')
        validated_data['role'] = 4
        userInstance = User.objects.create(**validated_data)
        medicoInstance=User.objects.get(id=medicoIdData)
        enfermeroInstance=User.objects.get(id=enfermeroIdData)
        familiarInstance=User.objects.get(id=familiarIdData)
        historiaClinicaInstance=HistoriaClinica.objects.get(id=historiaClinicaIdData)
        Paciente.objects.create(user=userInstance, medico=medicoInstance, enfermero=enfermeroInstance, familiar=familiarInstance, historiaClinica=historiaClinicaInstance)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        paciente = Paciente.objects.get(user=obj.id) 
        medico = User.objects.get(id=paciente.medico_id) 
        medicoDetail = Medico.objects.get(user_id=paciente.medico_id) 
        enfermero = User.objects.get(id=paciente.enfermero_id) 
        enfermeroDetail = Enfermero.objects.get(user_id=paciente.enfermero_id) 
        familiar = User.objects.get(id=paciente.familiar_id) 
        familiarDetail = Familiar.objects.get(user_id=paciente.familiar_id) 
        historiaClinica = HistoriaClinica.objects.get(id=paciente.historiaClinica_id) 
        historiaClinicaDetail = HistoriaClinica.objects.get(user_id=paciente.historiaClinica_id) 
              
        return {
                    'id': user.id, 
                    'username': user.username,
                    'nombre': user.nombre,
                    'apellido': user.apellido,
                    'celular': user.celular,
                    'direccion': user.direccion,
                    'email': user.email,
                    'role': user.role,
                    'medico': {
                        'username': medico.username,
                        'nombre': medico.nombre,
                        'apellido': medico.apellido,
                        'celular': medico.celular,
                        'direccion': medico.direccion,
                        'email': medico.email,
                        'especialidad': medicoDetail.especialidad
                    },
                    'enfermero': {
                        'username': enfermero.username,
                        'nombre': enfermero.nombre,
                        'apellido': enfermero.apellido,
                        'celular': enfermero.celular,
                        'direccion': enfermero.direccion,
                        'email': enfermero.email,
                        'area': enfermeroDetail.area
                    }, 
                    'familiar':{
                        'username': familiar.username,
                        'nombre': familiar.nombre,
                        'apellido': familiar.apellido,
                        'celular': familiar.celular,
                        'direccion': familiar.direccion,
                        'email': familiar.email,
                        'parentesco': familiarDetail.parentesco
                    },
                    'historiaClinica':{
                        '__all__'
                    }  
               
               
               
               
                }