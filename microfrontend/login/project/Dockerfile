# Etapa 1: Instalar dependencias y configurar el entorno de desarrollo
FROM node:18-slim AS dev

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo package.json y package-lock.json (o npm-shrinkwrap.json)
COPY package*.json ./

# Instalar las dependencias del proyecto
RUN npm install

# Copiar el código fuente al contenedor
COPY . .

# Exponer el puerto que usará Vite
EXPOSE 5173

# Ejecutar Vite en modo de desarrollo
CMD ["npm", "run", "dev"]