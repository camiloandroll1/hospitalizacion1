from rest_framework import status, views
from rest_framework.response import Response
from authApp.models.historiaClinica import HistoriaClinica
from authApp.serializers.historiaClinicaSerializer import HistoriaClinicaSerializer

class HistoriaClinicaDetailView(views.APIView):
    def get(self, request, *args, **kwargs):
        pk=kwargs['pk']
        historiaClinica = HistoriaClinica.objects.get(pk=pk)
        serializer = HistoriaClinicaSerializer(historiaClinica)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        pk=kwargs['pk']
        historiaClinica = HistoriaClinica.objects.get(pk=pk)
        historiaClinica.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        pk=kwargs['pk']
        historiaClinica = HistoriaClinica.objects.get(pk=pk)
        serializer = HistoriaClinicaSerializer(historiaClinica,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs):
        pk=kwargs['pk']
        historiaClinica = HistoriaClinica.objects.get(pk=pk)
        serializer = HistoriaClinicaSerializer(historiaClinica, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
