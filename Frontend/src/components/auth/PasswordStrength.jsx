import { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import zxcvbn from 'zxcvbn';
import { motion } from 'framer-motion';

const PasswordStrength = ({ password }) => {
  const [strength, setStrength] = useState(0);
  const [message, setMessage] = useState('');

  useEffect(() => {
    if (!password) {
      setStrength(0);
      setMessage('');
      return;
    }

    const result = zxcvbn(password);
    setStrength(result.score);

    const messages = [
      'Muy débil',
      'Débil',
      'Regular',
      'Buena',
      'Muy fuerte',
    ];
    setMessage(messages[result.score]);
  }, [password]);

  if (!password) return null;

  const getColor = (score) => {
    const colors = ['#ff4e42', '#ffa724', '#ffd000', '#9cc636', '#00b600'];
    return colors[score];
  };

  return (
    <div className="mt-2">
      <div className="h-1 w-full bg-gray-200 rounded-full overflow-hidden">
        <motion.div
          initial={{ width: 0 }}
          animate={{ width: `${(strength + 1) * 20}%` }}
          transition={{ duration: 0.3 }}
          style={{ backgroundColor: getColor(strength) }}
          className="h-full"
        />
      </div>
      <p
        className="text-xs mt-1"
        style={{ color: getColor(strength) }}
      >
        {message}
      </p>
    </div>
  );
};

PasswordStrength.propTypes = {
  password: PropTypes.string,
};

export default PasswordStrength;