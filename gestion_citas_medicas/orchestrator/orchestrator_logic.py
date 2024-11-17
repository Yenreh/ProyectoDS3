import uuid
from .models import Transaction, Appointment, Patient, Doctor
from .messaging import send_message, receive_response
import logging


logger = logging.getLogger(__name__)

def orchestrate_appointment(patient_id, doctor_id, date_time):
    transaction_id = uuid.uuid4()
    transaction_record = Transaction.objects.create(
        transaction_id=transaction_id,
        status='PENDING'
    )
    try:
        # Paso 1: Crear cita
        send_message('appointment_service', {
            'transaction_id': str(transaction_id),
            'patient_id': patient_id,
            'doctor_id': doctor_id,
            'date_time': date_time
        })
        response = receive_response(transaction_id)
        if response['status'] != 'SUCCESS':
            raise ValueError("Error en el microservicio de citas")

        # Paso 2: Actualizar historial
        send_message('history_service', {
            'transaction_id': str(transaction_id),
            'patient_id': patient_id,
            'action': 'appointment_created',
            'date_time': date_time
        })
        response = receive_response(transaction_id)
        if response['status'] != 'SUCCESS':
            raise ValueError("Error en el microservicio de historial")

        # Paso 3: Notificar
        send_message('notification_service', {
            'transaction_id': str(transaction_id),
            'patient_id': patient_id,
            'doctor_id': doctor_id,
            'message': 'Nueva cita creada',
            'date_time': date_time
        })
        response = receive_response(transaction_id)
        if response['status'] != 'SUCCESS':
            raise ValueError("Error en el microservicio de notificaciones")

        # Actualizar estado de la transacción y cita
        transaction_record.status = 'SUCCESS'
        transaction_record.save()

        # Crear la cita en la base de datos
        patient = Patient.objects.get(id=patient_id)
        doctor = Doctor.objects.get(id=doctor_id)
        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            date_time=date_time,
            status='CONFIRMED'
        )

    except ValueError as e:
        # Si hay un error en alguna etapa, cambiar el estado de la transacción a 'FAILED'
        transaction_record.status = 'FAILED'
        transaction_record.save()
        logger.error(f"Transacción fallida: {e}")
        compensate_appointment(transaction_id)
    except Exception as e:
        transaction_record.status = 'FAILED'
        transaction_record.save()
        logger.error(f"Error inesperado: {e}")
        compensate_appointment(transaction_id)

def compensate_appointment(transaction_id):
    try:
        # Eliminar la cita creada
        appointment = Appointment.objects.filter(transaction_id=transaction_id).first()
        if appointment:
            appointment.delete()

        # Simular compensaciones en microservicios
        send_message('history_service', {
            'transaction_id': str(transaction_id),
            'action': 'delete_entry'
        })
        send_message('notification_service', {
            'transaction_id': str(transaction_id),
            'action': 'cancel_notification'
        })
        logger.info(f"Compensación exitosa para la transacción {transaction_id}")

    except Exception as e:
        logger.error(f"Error durante la compensación de la transacción {transaction_id}: {e}")
