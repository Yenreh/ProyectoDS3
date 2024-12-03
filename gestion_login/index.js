import express from 'express';
import session from 'express-session';
import bodyParser from 'body-parser';
import cors from 'cors';
import dotenv from 'dotenv';  // Importar dotenv

import authRoutes from './routes/auth.js'; 
import userRoutes from './routes/users.js';

// Configurar dotenv para cargar las variables de entorno
dotenv.config();

const app = express();

// Configurar CORS
app.use(cors({
    origin: ['http://localhost:5174'],  // Agregar el nuevo puerto
    credentials: true
}));

// Configurar el body parser
app.use(bodyParser.json());

// Configuración de la sesión
app.use(session({
    secret: process.env.SESSION_SECRET,  // Usar la variable de entorno
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false } // Cambia a true si usas HTTPS en producción
}));

// Rutas de autenticación
app.use('/auth', authRoutes);
app.use('/users', userRoutes);

// Inicializar el servidor
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor en funcionamiento en el puerto ${PORT}`);
});
