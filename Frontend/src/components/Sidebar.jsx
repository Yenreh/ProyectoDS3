import { Link, useLocation } from 'react-router-dom';
import {
  AcademicCapIcon,
  BookOpenIcon,
  BeakerIcon,
  LightBulbIcon,
  StarIcon,
  UserGroupIcon,
  BuildingLibraryIcon
} from '@heroicons/react/24/outline';



const navigation = [
  { name: 'Informacion del grupo de Investigacion', href: '/grupo', icon: BookOpenIcon },
  { name: 'Prácticas de Investigación', href: '/practicas', icon: AcademicCapIcon },
  { name: 'Trabajos de Grado', href: '/trabajos-grado', icon: BookOpenIcon },
  { name: 'Proyectos de Investigación', href: '/proyectos', icon: BeakerIcon },
  { name: 'Líneas de Investigación', href: '/lineas', icon: LightBulbIcon },
  { name: 'Calificación ante Minciencias', href: '/calificaciones', icon: StarIcon },
  { name: 'Miembros del Grupo de Investigación', href: '/miembros', icon: UserGroupIcon },
  { name: 'Convenios del Grupo de Investigación', href: '/convenios', icon: BuildingLibraryIcon },
  { name: ' Gestion de Usuarios', href: '/usuarios', icon: BuildingLibraryIcon },
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
