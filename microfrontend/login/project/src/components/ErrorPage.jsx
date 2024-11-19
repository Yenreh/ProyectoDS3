import React from 'react';

const ErrorPage = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-red-50 to-red-100">
      <div className="max-w-lg w-full bg-white rounded-xl shadow-2xl p-8 mx-4">
        <div className="text-center">
          <div className="mb-6">
            <div className="bg-red-100 rounded-full w-20 h-20 flex items-center justify-center mx-auto">
              <span className="text-4xl">⚡</span>
            </div>
          </div>
          
          <h1 className="text-3xl font-bold text-gray-900 mb-4">
            Servicio Temporalmente No Disponible
          </h1>
          
          <div className="bg-red-50 border-l-4 border-red-500 p-4 mb-6">
            <p className="text-red-700">
              El Circuit Breaker está activo para proteger el sistema
            </p>
          </div>
          
          <p className="text-gray-600 mb-6">
            Nuestro sistema ha detectado un número elevado de intentos fallidos 
            y se ha activado temporalmente el mecanismo de protección. 
            Por favor, inténtelo de nuevo más tarde.
          </p>
          
          <div className="space-y-4">
            <div className="bg-gray-50 p-4 rounded-lg">
              <h3 className="font-semibold text-gray-700 mb-2">¿Qué puedo hacer?</h3>
              <ul className="text-left text-gray-600 space-y-2">
                <li className="flex items-center">
                  <span className="mr-2">•</span>
                  Espere unos minutos antes de intentar nuevamente
                </li>
                <li className="flex items-center">
                  <span className="mr-2">•</span>
                  Verifique sus credenciales
                </li>
                <li className="flex items-center">
                  <span className="mr-2">•</span>
                  Si el problema persiste, contacte con soporte técnico
                </li>
              </ul>
            </div>
            
            <button 
              onClick={() => window.location.reload()} 
              className="w-full bg-red-600 text-white py-3 px-4 rounded-lg hover:bg-red-700 transition duration-150 ease-in-out transform hover:-translate-y-0.5"
            >
              Intentar Nuevamente
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ErrorPage;