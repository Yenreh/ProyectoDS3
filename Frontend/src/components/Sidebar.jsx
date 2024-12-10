import { Link, useLocation } from 'react-router-dom';
import {
 
  UserGroupIcon,
  ClipboardDocumentIcon,
  ChatBubbleOvalLeftEllipsisIcon
} from '@heroicons/react/24/outline';



const navigation = [
  { name: 'Autenticacion', href: '/usuarios', icon: UserGroupIcon },
  { name: 'Citas', href: '/citas', icon: ClipboardDocumentIcon },
  { name: 'Comunicacion Tiempo Real', href: '/Comunicacion_TiempoReal', icon: ChatBubbleOvalLeftEllipsisIcon },
];

export default function Sidebar() {
  const location = useLocation();

  return (
    <div className="flex flex-col w-64 bg-mainColor min-h-screen">
      {/* Logo y título */}
      <div className="flex items-center h-20 px-5">
       
        <h1 className="text-white font-bold text-xl">Dashboard Administrador</h1>
      </div>

      {/* Navegación */}
      <nav className="mt-5 flex-1 px-4 space-y-4">
        {navigation.map((item) => {
          const isActive = location.pathname === item.href;
          return (
            <Link
              key={item.name}
              to={item.href}
              className={`${
                isActive
                  ? 'bg-white text-red-500 scale-105 shadow-lg'
                  : 'text-white hover:bg-white hover:text-red-500 hover:scale-105'
              } transform transition-all duration-300 flex flex-col items-center justify-center px-4 py-6 text-sm font-medium rounded-lg group`}
            >
              <item.icon
                className={`${
                  isActive
                    ? 'text-red-500'
                    : 'text-white group-hover:text-red-500'
                } h-8 w-8 transition-colors duration-300`}
                aria-hidden="true"
              />
              <span className="mt-2 text-center">{item.name}</span> {/* Centrado del nombre */}
            </Link>
          );
        })}
      </nav>
    </div>
  );
}
