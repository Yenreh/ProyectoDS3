import { Toaster } from 'react-hot-toast';
import LoginForm from './components/LoginForm';
import './App.css';

function App() {
  return (
    <>
      <Toaster 
        position="top-right"
        toastOptions={{
          style: {
            background: '#333',
            color: '#fff',
            borderRadius: '10px',
            padding: '16px',
          },
          success: {
            duration: 3000,
            iconTheme: {
              primary: '#4ade80',
              secondary: '#fff',
            },
          },
          error: {
            duration: 4000,
            iconTheme: {
              primary: '#ef4444',
              secondary: '#fff',
            },
          },
        }}
      />
      <LoginForm />
    </>
  );
}

export default App;