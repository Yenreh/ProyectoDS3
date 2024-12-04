# Usar la imagen oficial de Node.js basada en Alpine
FROM node:23-alpine

# Crear y establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el package.json y package-lock.json para instalar dependencias
# Copiar los archivos necesarios para instalar dependencias

COPY package.json . 
COPY package-lock.json .

# Instalar las dependencias
RUN npm install

# Copiar el resto de los archivos del backend al contenedor
COPY . .

# Exponer el puerto en el que corre el servidor de desarrollo (5174)
EXPOSE 5173

# Comando para arrancar el servidor de desarrollo del frontend
CMD ["npm", "run", "dev"]
