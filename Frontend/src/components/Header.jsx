import { useAuth } from '../contexts/AuthContext';
import { useNavigate } from 'react-router-dom';

export default function Header() {
  const { currentUser, logout } = useAuth();
  const navigate = useNavigate();

  async function handleLogout() {
    try {
      await logout();
      navigate('/');
    } catch (error) {
      console.error('Error al cerrar sesión:', error);
    }
  }

  return (
    <header className="bg-mainColor ">
      <div className="w-full px-10 py-4 flex justify-end items-center">
        <div className="flex items-center space-x-4">
          <span className="text-white">{currentUser?.email}</span>
          <button
            onClick={handleLogout}
            className="bg-white  px-4 py-2 rounded-md  transition-colors"
          >
            Cerrar Sesión
          </button>
        </div>
      </div>
    </header>
  );
  
  
}
