from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TransactionViewSet,
    PatientViewSet,
    DoctorViewSet,
    AppointmentViewSet,
    AppointmentHistoryViewSet,
)

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'appointment-history', AppointmentHistoryViewSet)
from .views import CreateAppointmentView, UpdateAppointmentView, DeleteAppointmentView

urlpatterns = [
    path('', include(router.urls)),  
    path('appointments/create/', CreateAppointmentView.as_view(), name='create_appointment'),
    path('appointments/update/<int:pk>/', UpdateAppointmentView.as_view(), name='update_appointment'),
    path('appointments/delete/<int:pk>/', DeleteAppointmentView.as_view(), name='delete_appointment'),
]
