import { useNavigate } from 'react-router-dom';
import {
  UserGroupIcon,
  ClipboardDocumentIcon,
  ChatBubbleOvalLeftEllipsisIcon


} from '@heroicons/react/24/outline';

const features = [
  {
    name: 'Comunicacion en tiempo real',
    description: 'No disponible',
    icon: ChatBubbleOvalLeftEllipsisIcon,
    href: '/Comunicacion_TiempoReal'
  },
  {
    name: 'Citas ',
    description: 'Gestión de citas medicas',
    icon: ClipboardDocumentIcon,
    href: '/citas'
  },
  {
    name: 'Autenticacion',
    description: 'Administración de cuestas para autenticacion',
    icon: UserGroupIcon,
    href: '/usuarios'
  }
  
];

export default function Dashboard() {
  const navigate = useNavigate();

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="mt-6">
        {/* Usar grid para las tarjetas */}
        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {features.map((feature) => (
            <div
              key={feature.name}
              className="relative group bg-white p-6 rounded-lg shadow-lg hover:shadow-2xl transition-all cursor-pointer"
              onClick={() => navigate(feature.href)}
            >
              <div>
                <span className="rounded-lg inline-flex p-3 bg-indigo-50 text-indigo-700 ring-4 ring-white">
                  <feature.icon className="h-6 w-6" aria-hidden="true" />
                </span>
              </div>
              <div className="mt-8">
                <h3 className="text-lg font-medium">
                  <span className="absolute inset-0" aria-hidden="true" />
                  {feature.name}
                </h3>
                <p className="mt-2 text-sm text-gray-500">
                  {feature.description}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
