import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import { motion } from 'framer-motion';
import { FiEye, FiEyeOff, FiMail, FiLock } from 'react-icons/fi';
import { toast } from 'react-hot-toast';
import InputField from './InputField';
import PasswordStrength from './PasswordStrength';
import { login } from '../../api/apis';  // Import login function from apis.js

const schema = yup.object().shape({
  email: yup
    .string()
    .email('Por favor, introduce un email válido')
    .required('El email es requerido'),
  password: yup
    .string()
    .min(8, 'La contraseña debe tener al menos 8 caracteres')
    .required('La contraseña es requerida'),
  rememberMe: yup.boolean(),
});

const LoginForm = () => {
  const [showPassword, setShowPassword] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [isResetting, setIsResetting] = useState(false);

  const {
    register,
    handleSubmit,
    watch,
    getValues,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(schema),
  });

  const password = watch('password', '');

  const handleResetPassword = async () => {
    const email = getValues('email');
    if (!email) {
      toast.error('Por favor, introduce tu email para restablecer la contraseña');
      return;
    }

    setIsResetting(true);
    // Implement your resetPassword logic here if necessary
    setIsResetting(false);
    toast.success('Se ha enviado un email para restablecer tu contraseña');
  };

  const onSubmit = async (data) => {
    setIsLoading(true);
    try {
      const { token } = await login(data.email, data.password);  // Call the login function from apis.js
      setIsLoading(false);
      toast.success('¡Bienvenido!');
      // You can save the token in local storage or context, or redirect the user
    } catch (error) {
      setIsLoading(false);
      toast.error(error.message);  // Show error message if login fails
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
        Iniciar Sesión
      </h2>

      <div className="space-y-4">
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

        <div className="flex items-center justify-between">
          <label className="flex items-center space-x-2">
            <input
              type="checkbox"
              {...register('rememberMe')}
              className="form-checkbox"
            />
            <span className="text-sm text-gray-600 dark:text-gray-300">
              Recordarme
            </span>
          </label>
          <button
            type="button"
            onClick={handleResetPassword}
            disabled={isResetting}
            className="text-sm text-blue-600 hover:text-blue-800 dark:text-blue-400"
          >
            {isResetting ? 'Enviando...' : '¿Olvidaste tu contraseña?'}
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
            'Iniciar Sesión'
          )}
        </button>

        <p className="text-center text-sm text-gray-600 dark:text-gray-300 mt-4">
          ¿No tienes una cuenta?{' '}
          <a href="/register" className="text-blue-600 hover:text-blue-800 dark:text-blue-400">
            Regístrate aquí
          </a>
        </p>
      </div>
    </motion.form>
  );
};

export default LoginForm;
