from django.http import JsonResponse
from .orchestrator_logic import orchestrate_appointment 
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction, Patient, Doctor, Appointment, AppointmentHistory
from .serializers import (
    TransactionSerializer,
    PatientSerializer,
    DoctorSerializer,
    AppointmentSerializer,
    AppointmentHistorySerializer,
)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentHistoryViewSet(viewsets.ModelViewSet):
    queryset = AppointmentHistory.objects.all()
    serializer_class = AppointmentHistorySerializer
    
class CreateAppointmentView(APIView):
   
    def post(self, request, *args, **kwargs):
        
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateAppointmentView(APIView):
    
    def get(self, request, pk, *args, **kwargs):
        
        try:
            
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({"error": "Cita no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
       
        try:
        
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({"error": "Cita no encontrada"}, status=status.HTTP_404_NOT_FOUND)

       
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class DeleteAppointmentView(APIView):
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            
            appointment = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({"error": "Cita no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        # Eliminamos la cita.
        appointment.delete()
        return Response({"message": "Cita eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)



