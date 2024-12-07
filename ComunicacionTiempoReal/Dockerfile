# Imagen base
FROM node:18-alpine

# Crear directorio de la aplicación
WORKDIR /app

# Copiar dependencias
COPY package.json package-lock.json ./

# Instalar dependencias
RUN npm install

# Copiar el código fuente
COPY . .

# Exponer el puerto
EXPOSE 8080

# Comando para iniciar el microservicio
CMD ["npm", "start"]
