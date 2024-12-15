import axios from 'axios';

// Instancia de axios para la API de time_communication
const timeCommunicationApi = axios.create({
  baseURL: import.meta.env.VITE_API_URL
    ? `${import.meta.env.VITE_API_URL}/time_communication`
    : "http://localhost:5000/time_communication", // Asegúrate de usar la URL correcta
  credentials: true, // Permite enviar cookies de sesión si es necesario
});

// Nueva API de "users"
const usersApi = axios.create({
  baseURL: import.meta.env.VITE_API_URL
    ? `${import.meta.env.VITE_API_URL}/users`
    : "http://localhost:5000/users",
  credentials: true,
});

const userApi = axios.create({
    baseURL: "http://localhost:5000",
    credentials: true,
});

export const getAllUser = () => userApi.get('/users');
export const createUser2 = () => userApi.post('/user');
export const getDoctors = () => userApi.get("/doctors");
export const getPacientes = () => userApi.get("/patients");


const appointmentApi = axios.create({
  baseURL: "http://localhost:5000",
  credentials: true,
});

export const getAppointments = () => appointmentApi.get('/appointments');

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


// Funciones para "usuarios"
export const getAllUsers = () => usersApi.get('/getUsers');
export const getUser = (uid) => usersApi.get(`/getUser/${uid}`);
export const createUser = (data) => usersApi.post('/createUser', data);
export const updateUser = (uid, data) => usersApi.put(`/updateUser/${uid}`, data);
export const deleteUser = (uid) => usersApi.delete(`/deleteUser/${uid}`);