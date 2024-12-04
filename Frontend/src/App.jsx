import { Toaster } from 'react-hot-toast';
import AuthLayout from './components/auth/AuthLayout';
import LoginForm from './components/auth/LoginForm';
import RegisterForm from './components/auth/RegisterForm';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Toaster position="top-right" />
      <AuthLayout>
        <Routes>
          {/* Redirige la ruta base / a /login */}
          <Route path="/" element={<Navigate to="/login" />} />
          
          {/* Definir las rutas para Login y Register */}
          <Route path="/login" element={<LoginForm />} />
          <Route path="/register" element={<RegisterForm />} />
        </Routes>
      </AuthLayout>
    </Router>
  );
}

export default App;

