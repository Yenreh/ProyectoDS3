import uuid
from .models import Transaction, Appointment, AppointmentHistory
import logging

logger = logging.getLogger(__name__)


def orchestrate_appointment(patient_id, doctor_id, date_time):
    transaction_id = uuid.uuid4()
    transaction_record = Transaction.objects.create(
        transaction_id=transaction_id,
        status='PENDING'
    )
    try:
        # 1 - Crear la cita en appointmens
        appointment_id = uuid.uuid4()
        Appointment.objects.create(
            appointment_id=appointment_id,
            patient_id=patient_id,
            doctor_id=doctor_id,
            date_time=date_time,
            status='PENDING'
        )

        # 2 -Obtener el id de la cita creada y guardarlo en la transacción
        transaction_record.appointment_id = Appointment.objects.get(appointment_id=appointment_id)
        transaction_record.save()

        # 3- Guardar la cita en el historial

        appointment_history_id = uuid.uuid4()
        AppointmentHistory.objects.create(
            history_id=appointment_history_id,
            patient_id=patient_id,
            appointment_id=appointment_id,
            action='CREATED')

        # 3- Actualizar estado de la transacción y cita
        transaction_record.status = 'SUCCESS'
        transaction_record.save()

        # Verificar que los datos de la cita sean válidos
        if not patient_id or not doctor_id or not date_time:
            raise ValueError("Datos inválidos")

        # Verificar que un mismo doctor no tenga dos citas en estado PENDING o CONFIRMED al mismo tiempo
        # y el appointment_id no igual a la cita creada
        if Appointment.objects.filter(doctor_id=doctor_id, status__in=['PENDING', 'CONFIRMED'], date_time=date_time).exclude(appointment_id=appointment_id).exists():
            raise ValueError("El doctor ya tiene una cita pendiente o confirmada")

        # Verificar que un mismo paciente no tenga dos citas en estado PENDING o CONFIRMED  al mismo tiempo
        # y el appointment_id no igual a la cita creada
        if Appointment.objects.filter(patient_id=patient_id, status__in=['PENDING', 'CONFIRMED'], date_time=date_time).exclude(appointment_id=appointment_id).exists():
            raise ValueError("El paciente ya tiene una cita pendiente o confirmada")

        return True

    except ValueError as e:
        # Si hay un error en alguna etapa, cambiar el estado de la transacción a 'FAILED'
        transaction_record.status = 'FAILED'
        transaction_record.save()
        logger.error(f"Transacción fallida: {e}")
        return compensate_appointment(transaction_id)
    except Exception as e:
        transaction_record.status = 'FAILED'
        transaction_record.save()
        logger.error(f"Error inesperado: {e}")
        return compensate_appointment(transaction_id)


def compensate_appointment(transaction_id):
    try:
        # 1 - Obtener la transacción
        transaction = Transaction.objects.filter(transaction_id=transaction_id).first()
        appointment_id = transaction.appointment_id.appointment_id

        # 2 - Se Cancela la cita
        appointment = Appointment.objects.filter(appointment_id=appointment_id).first()
        Appointment.objects.filter(appointment_id=appointment_id).update(status='CANCELLED')

        # 3 - Se guarda la acción en el historial
        AppointmentHistory.objects.create(
            patient_id=appointment.patient_id,
            appointment_id=appointment_id,
            action='CANCELLED'
        )

        return False
    except Exception as e:
        logger.error(f"Error durante la compensación de la transacción {transaction_id}: {e}")
