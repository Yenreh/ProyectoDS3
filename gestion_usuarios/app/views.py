from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import action

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['get'])
    def doctors(self, request):
        """Endpoint para traer todos los usuarios de tipo 'doctor'"""
        doctors = User.objects.filter(user_type='doctor')
        serializer = self.get_serializer(doctors, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def pacientes(self, request):
        """Endpoint para traer todos los usuarios de tipo 'paciente'"""
        pacientes = User.objects.filter(user_type='paciente')
        serializer = self.get_serializer(pacientes, many=True)
        return Response(serializer.data)