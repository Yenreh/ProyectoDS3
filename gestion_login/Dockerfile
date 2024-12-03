# Usar la imagen oficial de Node.js basada en Alpine
FROM node:23-alpine

# Crear y establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el package.json y package-lock.json para instalar dependencias
COPY Backend/package*.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto de los archivos del backend al contenedor
COPY Backend/ .

# Exponer el puerto en el que corre la API (3000)
EXPOSE 3000


CMD ["npm", "run","dev"]
