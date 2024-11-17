from django.db import models
import uuid


class Appointment(models.Model):
    appointment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.IntegerField(default=None, null=True, blank=True)
    doctor_id = models.IntegerField(default=None, null=True, blank=True)
    date_time = models.DateTimeField(default=None, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pendiente'),
            ('CONFIRMED', 'Confirmada'),
            ('CANCELLED', 'Cancelada')
        ],
        default='PENDING'
    )


class Transaction(models.Model):
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pendiente'),
            ('SUCCESS', 'Éxito'),
            ('FAILED', 'Fallido')
        ]
    )
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AppointmentHistory(models.Model):
    history_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.IntegerField(default=None, null=True, blank=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)  # Ej: Created, Updated, Cancelled
    date_time = models.DateTimeField(auto_now_add=True)
