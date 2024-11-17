from django.http import JsonResponse
from .orchestrator_logic import orchestrate_appointment 
from rest_framework import viewsets
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



