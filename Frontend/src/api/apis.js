import axios from 'axios';

// Instancia de axios para la API de time_communication
const timeCommunicationApi = axios.create({
  baseURL: import.meta.env.VITE_API_URL
    ? `${import.meta.env.VITE_API_URL}/time_communication`
    : "http://localhost:5000/time_communication", // Asegúrate de usar la URL correcta
  credentials: true, // Permite enviar cookies de sesión si es necesario
});

// Función para redirigir a la URL de time_communication
export const getTimeCommunication = async () => {
  try {
    // Redirige a la URL usando el baseURL configurado en timeCommunicationApi
    window.location.href = timeCommunicationApi.defaults.baseURL;
  } catch (error) {
    console.error('Error al redirigir:', error.message);
    throw new Error('Error al redirigir a la URL de time_communication');
  }
};

// Exporta la instancia para poder usarla en cualquier lugar
export { timeCommunicationApi };
