# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos de la aplicación
COPY requirements.txt /app/

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación Flask al contenedor
COPY . /app/

# Exponer el puerto que utilizará la aplicación
EXPOSE 9002

# Comando para ejecutar la aplicación cuando el contenedor se inicie
CMD ["python", "login_service.py"]