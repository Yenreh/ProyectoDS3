import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import { motion } from 'framer-motion';
import { FiEye, FiEyeOff, FiMail, FiLock, FiUser } from 'react-icons/fi';
import { toast } from 'react-hot-toast';
import InputField from './InputField';
import PasswordStrength from './PasswordStrength';
import { createUser } from '../../api/apis';  // Importa la función createUser de apis.js

// Esquema de validación con Yup
const schema = yup.object().shape({
  name: yup
    .string()
    .required('El nombre es requerido')
    .min(2, 'El nombre debe tener al menos 2 caracteres'),
  displayName: yup
    .string()
    .required('El nombre de usuario es requerido')
    .min(2, 'El nombre de usuario debe tener al menos 2 caracteres'),
  email: yup
    .string()
    .email('Por favor, introduce un email válido')
    .required('El email es requerido'),
  password: yup
    .string()
    .min(8, 'La contraseña debe tener al menos 8 caracteres')
    .matches(
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/,
      'La contraseña debe contener al menos una mayúscula, una minúscula y un número'
    )
    .required('La contraseña es requerida'),
  confirmPassword: yup
    .string()
    .oneOf([yup.ref('password')], 'Las contraseñas no coinciden')
    .required('Por favor, confirma tu contraseña'),
});

const RegisterForm = () => {
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(schema),
  });

  const password = watch('password', '');

  // Función de envío del formulario
  const onSubmit = async (data) => {
    setIsLoading(true);

    const { name, displayName, email, password } = data;

    try {
      // Llamar a la función createUser para registrar al usuario
      const { message } = await createUser({ name, displayName, email, password });
      toast.success(message || '¡Registro exitoso!');
      // Aquí puedes redirigir al usuario o actualizar el estado de la aplicación
    } catch (error) {
      toast.error(error.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <motion.form
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.3 }}
      className="bg-white dark:bg-gray-800 p-8 rounded-lg shadow-lg"
      onSubmit={handleSubmit(onSubmit)}
    >
      <h2 className="text-2xl font-bold text-center mb-6 text-gray-800 dark:text-white">
        Crear Cuenta
      </h2>

      <div className="space-y-4">
        <InputField
          label="Nombre"
          type="text"
          icon={<FiUser />}
          error={errors.name?.message}
          {...register('name')}
        />

        <InputField
          label="Nombre de Usuario"
          type="text"
          icon={<FiUser />}
          error={errors.displayName?.message}  // Mostramos el error de displayName
          {...register('displayName')}  // Añadido el registro para displayName
        />

        <InputField
          label="Email"
          type="email"
          icon={<FiMail />}
          error={errors.email?.message}
          {...register('email')}
        />

        <div className="relative">
          <InputField
            label="Contraseña"
            type={showPassword ? 'text' : 'password'}
            icon={<FiLock />}
            error={errors.password?.message}
            {...register('password')}
          />
          <button
            type="button"
            className="absolute right-3 top-9 text-gray-500"
            onClick={() => setShowPassword(!showPassword)}
          >
            {showPassword ? <FiEyeOff /> : <FiEye />}
          </button>
        </div>

        <PasswordStrength password={password} />

        <div className="relative">
          <InputField
            label="Confirmar Contraseña"
            type={showConfirmPassword ? 'text' : 'password'}
            icon={<FiLock />}
            error={errors.confirmPassword?.message}
            {...register('confirmPassword')}
          />
          <button
            type="button"
            className="absolute right-3 top-9 text-gray-500"
            onClick={() => setShowConfirmPassword(!showConfirmPassword)}
          >
            {showConfirmPassword ? <FiEyeOff /> : <FiEye />}
          </button>
        </div>

        <button
          type="submit"
          disabled={isLoading}
          className="w-full py-2 px-4 bg-blue-600 hover:bg-blue-700 text-white rounded-md transition-colors duration-200 disabled:opacity-50"
        >
          {isLoading ? (
            <span className="flex items-center justify-center">
              <motion.div
                animate={{ rotate: 360 }}
                transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}
                className="w-5 h-5 border-2 border-white border-t-transparent rounded-full"
              />
            </span>
          ) : (
            'Registrarse'
          )}
        </button>

        <p className="text-center text-sm text-gray-600 dark:text-gray-300 mt-4">
          ¿Ya tienes una cuenta?{' '}
          <a href="/login" className="text-blue-600 hover:text-blue-800 dark:text-blue-400">
            Inicia sesión aquí
          </a>
        </p>
      </div>
    </motion.form>
  );
};

export default RegisterForm;
