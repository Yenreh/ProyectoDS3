// src/components/Users.jsx

import { PlusCircleIcon, TrashIcon, PencilIcon, EyeIcon, EyeSlashIcon } from '@heroicons/react/24/outline';
import useUsers from './UsuariosLogic';
import '../styles/users.css';

export default function Users() {
  const {
    users,
    loading,
    error,
    isFormVisible,
    formData,
    showPassword,
    passwordError,
    emailError,
    setFormData,
    setIsFormVisible,
    setShowPassword,
    handleSubmit,
    handleEdit,
    handleDelete,
    handleCancel,
  } = useUsers();

  if (loading) return <div className="text-center mt-8">Cargando...</div>;
  if (error) return <div className="text-red-600 text-center mt-8">{error}</div>;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      {/* Formulario de creación o edición */}
      {isFormVisible && (
        <form onSubmit={handleSubmit} className="form-container">
          <button type="button" onClick={handleCancel} className="cancel-btn">
            Cancelar
          </button>

          <div>
            <label className="block text-sm font-medium text-gray-700">Email</label>
            <input
              type="email"
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              className="form-input"
              required
            />
            {emailError && <p className="form-error">{emailError}</p>}
          </div>

          <div className="relative">
            <label className="block text-sm font-medium text-gray-700">Contraseña</label>
            <input
              type={showPassword ? 'text' : 'password'}
              value={formData.password}
              onChange={(e) => setFormData({ ...formData, password: e.target.value })}
              className="form-input pr-10"
            />
            <button type="button" onClick={() => setShowPassword(!showPassword)} className="show-password-btn">
              {showPassword ? <EyeSlashIcon className="w-6 h-6 text-gray-500" /> : <EyeIcon className="w-6 h-6 text-gray-500" />}
            </button>
            {passwordError && <p className="form-error">{passwordError}</p>}
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700">Nombre(s) y Apellido(s)</label>
            <input
              type="text"
              value={formData.displayName}
              onChange={(e) => setFormData({ ...formData, displayName: e.target.value })}
              className="form-input"
              required
            />
          </div>

          <button type="submit" className="create-user-btn">
            {formData.uid ? 'Actualizar Usuario' : 'Crear Usuario'}
          </button>
        </form>
      )}

      {/* Tabla de usuarios */}
      <div className="table-container">
        <table className="table">
          <thead>
            <tr>
              <th>Email</th>
              <th>Nombre(s) y Apellido(s)</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user.uid}>
                <td>{user.email}</td>
                <td>{user.displayName}</td>
                <td>
                  <button onClick={() => handleEdit(user)} className="action-btn">
                    <PencilIcon className="w-5 h-5 inline" />
                  </button>
                  <button onClick={() => handleDelete(user.uid)} className="delete-btn">
                    <TrashIcon className="w-5 h-5 inline" />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <button onClick={() => setIsFormVisible(true)} className="create-user-btn">
        <PlusCircleIcon className="w-6 h-6 mr-2" />
        Crear Usuario
      </button>
    </div>
  );
}







