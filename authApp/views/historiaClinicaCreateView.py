from rest_framework import status, views
from rest_framework.response import Response
from authApp.models.historiaClinica import HistoriaClinica
from authApp.serializers.historiaClinicaSerializer import HistoriaClinicaSerializer
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings

class HistoriaClinicaCreateView(views.APIView):
    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        valid_data['user_id']
        historiasClinicas = HistoriaClinica.objects.all()
        serializer = HistoriaClinicaSerializer(historiasClinicas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = HistoriaClinicaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data, status=status.HTTP_201_CREATED)
