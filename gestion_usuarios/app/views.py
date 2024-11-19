from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.utils import IntegrityError
from django.db import transaction
from rest_framework import status
from django.forms.models import model_to_dict


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
    
    def create(self, request, *args, **kwargs):
        """Reemplaza createUser con la lógica de create_user_with_saga"""
        # Inicia una transacción
        with transaction.atomic():
            try:
                # Crear el usuario inicialmente sin validar duplicados
                serializer = self.get_serializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    # Validar datos antes de guardar
                    self.validate_data(serializer.validated_data)

                    # Si la validación pasa, guardar el usuario
                    user = serializer.save()
                    user_id = user.id
                    print("ID del usuario creado:", user_id)

                    # Obtener todos los campos del usuario como un diccionario
                    user_data = model_to_dict(user)
                    print("Datos del usuario en un diccionario:", user_data)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                # Si ocurre un error de integridad, como duplicados, deshacemos la transacción
                transaction.set_rollback(True)
                return Response(
                    {"detail": "Datos duplicados detectados. Usuario eliminado."},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
    def validate_data(self, data):
        """Valida si ya existe un usuario con el mismo cc_user o professional_id"""
        cc_user = data.get("cc_user")
        professional_id = data.get("professional_id")

        # Verificar si ya existe un usuario con el mismo cc_user o professional_id
        if User.objects.filter(cc_user=cc_user).exists():
            raise IntegrityError("Ya existe un usuario con el mismo cc_user.")

        if User.objects.filter(professional_id=professional_id).exists():
            raise IntegrityError("Ya existe un usuario con el mismo professional_id.")
    

