const express = require('express');
const path = require('path');
const helmet = require('helmet');
const opossum = require('opossum'); // Librería para Circuit Breaker

const app = express();
const port = 8080;

// Middleware de seguridad
app.use(helmet());

// Middleware para parsear datos JSON
app.use(express.json());

// Servir archivos estáticos desde la carpeta 'public'
app.use(express.static(path.join(__dirname, 'public')));

// Simulando un servicio externo que podría fallar
const servicioExterno = () => {
  return new Promise((resolve, reject) => {
    // Simulamos un fallo aleatorio en el servicio externo
    const fallo = Math.random() < 0.5; // 50% de probabilidades de fallo
    if (fallo) {
      reject(new Error('Error en el servicio externo'));
    } else {
      resolve('Respuesta exitosa del servicio externo');
    }
  });
};

// Configuración del Circuit Breaker
const opciones = {
  timeout: 5000, // Tiempo máximo para completar la operación
  errorThresholdPercentage: 50, // Umbral de errores para abrir el circuito
  resetTimeout: 30000, // Tiempo después del cual el circuito se restablecerá
};

const circuito = new opossum(servicioExterno, opciones);

// Forzar que el Circuit Breaker esté siempre abierto
circuito.open();

// Ruta principal
app.get('/TimeComunication', async (req, res) => {
  try {
    // Siempre forzamos el Circuit Breaker a estar abierto
    circuito.open();  // Asegura que el Circuit Breaker esté siempre abierto

    console.log('Circuito abierto, redirigiendo a 410.html');
    // Redirigimos siempre a 410.html debido a que el Circuit Breaker está abierto
    res.status(410).sendFile(path.join(__dirname, 'public', '410.html'));
  } catch (error) {
    // Si ocurre un error inesperado, manejamos la excepción y redirigimos a 410.html
    console.error(`Error en la ruta '/TimeComunication': ${error.message}`);
    res.status(410).sendFile(path.join(__dirname, 'public', '410.html'));
  }
});

// Inicia el servidor
app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});
