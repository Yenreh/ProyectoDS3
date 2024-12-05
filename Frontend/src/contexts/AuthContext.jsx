import { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';

// Crear el contexto de autenticación
const AuthContext = createContext();

export function useAuth() {
  return useContext(AuthContext);
}

// Instancia de axios para la API de usuarios
const usersApi = axios.create({
  baseURL: import.meta.env.VITE_API_URL
    ? `${import.meta.env.VITE_API_URL}/users`
    : "http://localhost:5000/users",
  withCredentials: true, // Cambié "credentials" por "withCredentials"
});

const authApi = axios.create({
  baseURL: import.meta.env.VITE_API_URL
    ? `${import.meta.env.VITE_API_URL}/auth`
    : "http://localhost:5000/auth",
  withCredentials: true, // Cambié "credentials" por "withCredentials"
});

// Función para registrar un nuevo usuario
const createUser = async (data) => {
  try {
    const response = await usersApi.post('/createUser', data);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.message || 'Error al crear el usuario');
  }
};

// Proveedor de autenticación
export function AuthProvider({ children }) {
  const [currentUser, setCurrentUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Función para hacer login usando el backend
  async function login(email, password) {
    try {
      const response = await authApi.post('/login', { email, password });
      setCurrentUser(response.data.user);
      return response.data;
    } catch (error) {
      console.error('Error de login:', error);
      throw new Error(error.response?.data?.message || 'Error en el login');
    }
  }

  // Función para registrar o hacer login
  async function ensureAuthenticated(email, password, additionalData = {}) {
    try {
      await login(email, password); // Intentamos hacer login primero
    } catch (error) {
      try {
        const user = await createUser({ email, password, ...additionalData });
        setCurrentUser(user); // Autenticar automáticamente después del registro
        return user;
      } catch (error) {
        console.error('Error de registro:', error);
        throw error;
      }
    }
  }

  // Función para hacer logout usando el backend
  async function logout() {
    try {
      const response = await authApi.post('/logout', null, {
        withCredentials: true, // Asegura que las cookies se envíen
      });

      if (response.status !== 200) {
        throw new Error(response.data?.message || 'Error al cerrar sesión');
      }

      setCurrentUser(null); // Limpiar el estado del usuario
      return response.data;
    } catch (error) {
      console.error('Error de logout:', error);
      throw new Error(error.response?.data?.message || 'Error al cerrar sesión');
    }
  }

  // Comprobar el estado de la autenticación al cargar la página
  useEffect(() => {
    const checkSession = async () => {
      try {
        const response = await authApi.get('/check', { withCredentials: true });
        if (response.status === 200) {
          setCurrentUser(response.data.user);
        } else {
          setCurrentUser(null);
        }
      } catch (error) {
        setCurrentUser(null);
        console.error('Error al verificar la sesión:', error);
      }
      setLoading(false);
    };

    checkSession();
  }, []);

  const value = {
    currentUser,
    login,
    logout,
    ensureAuthenticated, // Incluir la función `ensureAuthenticated`
  };

  return (
    <AuthContext.Provider value={value}>
      {!loading && children}
    </AuthContext.Provider>
  );
}
