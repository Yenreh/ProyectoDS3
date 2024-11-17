import { useState } from 'react';
import axios from 'axios';
import toast from 'react-hot-toast';
import ErrorPage from './ErrorPage';

const LoginForm = () => {
  const [credentials, setCredentials] = useState({
    username: '',
    password: ''
  });
  const [loading, setLoading] = useState(false);
  const [isCircuitBreakerActive, setIsCircuitBreakerActive] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCredentials(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await axios.post('http://localhost:5000/login', credentials);
      toast.success('¡Inicio de sesión exitoso!');
      console.log('Login exitoso:', response.data);
    } catch (error) {
      if (error.response) {
        const status = error.response.status;
        if (status === 503) {
          setIsCircuitBreakerActive(true);
          toast.error('Servicio temporalmente no disponible debido a la activación del Circuit Breaker.', {
            duration: 5000,
            icon: '⚡'
          });
        } else if (status === 401) {
          toast.error('Usuario o contraseña incorrectos');
        } else {
          toast.error('Ocurrió un error inesperado');
        }
      } else {
        toast.error('Error de conexión. Por favor, verifique su conexión a internet.');
      }
    } finally {
      setLoading(false);
    }
  };

  if (isCircuitBreakerActive) {
    return <ErrorPage />;
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-100 to-indigo-100 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full bg-white rounded-xl shadow-2xl p-8 space-y-8">
        <div className="text-center">
          <h2 className="text-4xl font-bold text-gray-900 mb-2">
            Bienvenido
          </h2>
          <p className="text-gray-600">
            Por favor, ingrese sus credenciales
          </p>
        </div>
        
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <div className="space-y-4">
            <div>
              <label htmlFor="username" className="block text-sm font-medium text-gray-700 mb-1">
                Usuario
              </label>
              <input
                id="username"
                name="username"
                type="text"
                required
                className="appearance-none relative block w-full px-4 py-3 border border-gray-300 rounded-lg placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition duration-150 ease-in-out"
                placeholder="Ingrese su usuario"
                value={credentials.username}
                onChange={handleChange}
              />
            </div>
            <div>
              <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-1">
                Contraseña
              </label>
              <input
                id="password"
                name="password"
                type="password"
                required
                className="appearance-none relative block w-full px-4 py-3 border border-gray-300 rounded-lg placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition duration-150 ease-in-out"
                placeholder="Ingrese su contraseña"
                value={credentials.password}
                onChange={handleChange}
              />
            </div>
          </div>

          <div>
            <button
              type="submit"
              disabled={loading}
              className={`group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-lg text-white transition duration-150 ease-in-out ${
                loading 
                  ? 'bg-indigo-400 cursor-not-allowed' 
                  : 'bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-4 focus:ring-indigo-500 focus:ring-opacity-50 transform hover:-translate-y-0.5'
              }`}
            >
              {loading ? 'Iniciando sesión...' : 'Iniciar Sesión'}
            </button>
          </div>
        </form>

        <div className="text-center text-sm text-gray-600">
          ¿Olvidó su contraseña? <a href="#" className="font-medium text-indigo-600 hover:text-indigo-500">Recuperar acceso</a>
        </div>
      </div>
    </div>
  );
};

export default LoginForm;