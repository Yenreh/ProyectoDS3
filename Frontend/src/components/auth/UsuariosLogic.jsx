// src/hooks/useUsers.jsx

import { useState, useEffect } from 'react';
import { getAllUsers, createUser, updateUser, deleteUser } from '../../api/apis';

export default function useUsers() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isFormVisible, setIsFormVisible] = useState(false);
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    displayName: '',
    uid: null,
  });
  const [showPassword, setShowPassword] = useState(false);
  const [passwordError, setPasswordError] = useState('');
  const [emailError, setEmailError] = useState('');

  // Fetch all users
  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const response = await getAllUsers();
      setUsers(response.data.users); // Assuming response contains users
    } catch (err) {
      setError('Error al cargar los usuarios');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Validate password
  const validatePassword = (password) => {
    if (password.length < 6) {
      setPasswordError('La contraseña debe tener al menos 6 caracteres');
      return false;
    }
    setPasswordError('');
    return true;
  };

  // Validate email
  const validateEmail = (email) => {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailRegex.test(email)) {
      setEmailError('Por favor, ingresa un correo electrónico válido');
      return false;
    }
    setEmailError('');
    return true;
  };

  // Handle form submit
  const handleSubmit = async (e) => {
    e.preventDefault();
    const isEmailValid = validateEmail(formData.email);
    const isPasswordValid = formData.password ? validatePassword(formData.password) : true;

    if (!isEmailValid || !isPasswordValid) {
      return;
    }

    const dataToSubmit = { ...formData };
    if (!formData.password) {
      delete dataToSubmit.password; // Do not include password if it's empty
    }

    try {
      if (formData.uid) {
        // Update existing user
        await updateUser(formData.uid, dataToSubmit);
      } else {
        // Create a new user
        await createUser(dataToSubmit);
      }
      setIsFormVisible(false);
      setFormData({ email: '', password: '', displayName: '', uid: null });
      await fetchUsers();
    } catch (err) {
      setError('Error al guardar el usuario');
      console.error(err);
    }
  };

  // Handle edit user
  const handleEdit = (user) => {
    setFormData({
      email: user.email,
      password: '',
      displayName: user.displayName || '',
      uid: user.uid,
    });
    setIsFormVisible(true);
  };

  // Handle delete user
  const handleDelete = async (userId) => {
    try {
      await deleteUser(userId);
      setUsers(users.filter((user) => user.uid !== userId));
    } catch (err) {
      setError('Error al eliminar el usuario');
      console.error(err);
    }
  };

  // Handle cancel form
  const handleCancel = () => {
    setIsFormVisible(false);
    setFormData({ email: '', password: '', displayName: '', uid: null });
  };

  return {
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
  };
}