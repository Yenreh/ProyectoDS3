import { Toaster } from 'react-hot-toast';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import PrivateRoute from './components/PrivateRoute';
import Dashboard from './components/Dashboard';
import LoginForm from './components/auth/LoginForm';
import RegisterForm from './components/auth/RegisterForm';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import ComunicacionTiempoReal from './components/ComunicacionTiempoReal';  // Asegúrate de importar el componente

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="min-h-screen" style={{ backgroundColor: 'rgb(31, 41, 55)' }}>
          <Toaster />
          <Routes>
            {/* Rutas públicas */}
            <Route path="/login" element={<LoginForm />} />
            <Route path="/register" element={<RegisterForm />} />

            {/* Rutas protegidas */}
            <Route
              path="/*"
              element={
                <PrivateRoute>
                  <div className="flex">
                    <Sidebar />
                    <div className="flex-1">
                      <Header className="bg-blue shadow-md" />
                      <main className="flex-1 p-6">
                        <Routes>
                          {/* Ruta del dashboard */}
                          <Route
                            path="/"
                            element={
                              <div className="bg-white p-6 rounded-lg shadow-lg">
                                <Dashboard />
                              </div>
                            }
                          />
                          {/* Nueva ruta para /Comunicacion_TiempoReal */}
                          <Route
                            path="/Comunicacion_TiempoReal"
                            element={
                              <div className="bg-white p-6 rounded-lg shadow-lg">
                                <ComunicacionTiempoReal />
                              </div>
                            }
                          />
                        </Routes>
                      </main>
                    </div>
                  </div>
                </PrivateRoute>
              }
            />
          </Routes>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;

