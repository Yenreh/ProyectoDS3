from rest_framework import serializers
from .models import Transaction, Appointment, AppointmentHistory

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class AppointmentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentHistory
        fields = '__all__'