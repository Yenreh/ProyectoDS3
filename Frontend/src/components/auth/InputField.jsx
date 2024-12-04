import { forwardRef } from 'react';
import PropTypes from 'prop-types';
import { motion } from 'framer-motion';

const InputField = forwardRef(
  ({ label, type, icon, error, ...props }, ref) => {
    return (
      <div className="space-y-1">
        <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">
          {label}
        </label>
        <div className="relative">
          <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-gray-500">
            {icon}
          </div>
          <input
            ref={ref}
            type={type}
            className={`block w-full pl-10 pr-3 py-2 border ${
              error
                ? 'border-red-500 focus:ring-red-500 focus:border-red-500'
                : 'border-gray-300 focus:ring-blue-500 focus:border-blue-500'
            } rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 transition-all duration-200 dark:bg-gray-700 dark:border-gray-600 dark:text-white`}
            {...props}
          />
        </div>
        {error && (
          <motion.p
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-sm text-red-600 dark:text-red-400"
          >
            {error}
          </motion.p>
        )}
      </div>
    );
  }
);

InputField.propTypes = {
  label: PropTypes.string.isRequired,
  type: PropTypes.string.isRequired,
  icon: PropTypes.node,
  error: PropTypes.string,
};

InputField.displayName = 'InputField';

export default InputField;