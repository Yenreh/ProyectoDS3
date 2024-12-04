import axios from 'axios';

// Instancia de axios para la API de autenticación
const authApi = axios.create({
  baseURL: import.meta.env.VITE_API_URL
    ? `${import.meta.env.VITE_API_URL}/auth`
    : "http://localhost:5000/auth",  // Asegúrate de usar la URL correcta para la autenticación
    credentials: true, // Permite enviar cookies de sesión si es necesario
});

// Instancia de axios para la API de usuarios
const usersApi = axios.create({
  baseURL: import.meta.env.VITE_API_URL
    ? `${import.meta.env.VITE_API_URL}/users`
    : "http://localhost:5000/users",  // Asegúrate de usar la URL correcta para los usuarios
  credentials: true,  // Permite enviar cookies de sesión si es necesario
});

// Funciones para la autenticación (login, logout)
export const login = async (email, password) => {
  try {
    const response = await authApi.post('/login', { email, password });
    return response.data;  // Retorna los datos de la respuesta (por ejemplo, token de acceso)
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al iniciar sesión');
  }
};

export const logout = async () => {
  try {
    const response = await authApi.post('/logout');
    return response.data;  // Retorna los datos de la respuesta (confirmación de logout)
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al cerrar sesión');
  }
};

// Funciones para gestión de usuarios (CRUD)
export const getAllUsers = async () => {
  try {
    const response = await usersApi.get('/getUsers');
    return response.data;  // Retorna la lista de usuarios
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al obtener los usuarios');
  }
};

export const getUser = async (uid) => {
  try {
    const response = await usersApi.get(`/getUser/${uid}`);
    return response.data;  // Retorna los datos de un usuario específico
  } catch (error) {
    throw new Error(error.response?.data?.message || `Error al obtener el usuario ${uid}`);
  }
};

export const createUser = async (data) => {
  try {
    const response = await usersApi.post('/createUser', data);
    return response.data;  // Retorna los datos del nuevo usuario creado
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al crear el usuario');
  }
};

export const updateUser = async (uid, data) => {
  try {
    const response = await usersApi.put(`/updateUser/${uid}`, data);
    return response.data;  // Retorna los datos del usuario actualizado
  } catch (error) {
    throw new Error(error.response?.data?.message || `Error al actualizar el usuario ${uid}`);
  }
};

export const deleteUser = async (uid) => {
  try {
    const response = await usersApi.delete(`/deleteUser/${uid}`);
    return response.data;  // Retorna una confirmación de eliminación del usuario
  } catch (error) {
    throw new Error(error.response?.data?.message || `Error al eliminar el usuario ${uid}`);
  }
};

// Exporta las instancias para poder usarlas en cualquier lugar
export { authApi, usersApi };
