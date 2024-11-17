from django.urls import path, include, re_path
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

urlpatterns = [
    path('', include(router.urls)),
]
