import express from 'express';
import { auth } from '../config.js';
import { signInWithEmailAndPassword } from 'firebase/auth'; // Asegúrate de importar esto

const router = express.Router();

// Ruta para iniciar sesión con correo y contraseña
router.post('/login', async (req, res) => {
    const { email, password } = req.body;

    try {
        const userCredential = await signInWithEmailAndPassword(auth, email, password); // Asegúrate de pasar auth aquí
        const user = userCredential.user;
        req.session.user = user;  // Guarda el usuario en la sesión
        res.status(200).json({ message: 'Autenticación exitosa', user });
    } catch (error) {
        res.status(401).json({ message: 'Error de autenticación: correo o contraseña incorrectos', error: error.message });
    }
});

// Ruta para cerrar sesión
router.post('/logout', (req, res) => {
    req.session.destroy((err) => {
        if (err) {
            return res.status(500).json({ message: 'Error al cerrar sesión' });
        }
        res.status(200).json({ message: 'Sesión cerrada correctamente' });
    });
});

export default router;
