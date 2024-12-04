import express from 'express'; 
import admin from '../firebaseAdmin.js'; 

const router = express.Router();

// Obtener usuarios
router.get('/getUsers', async (req, res) => {
  const { uid } = req.query;  
  try {
    let result = await admin.auth().listUsers(1000);
    const userRecords = result.users;

    if (uid) {
      const user = userRecords.find(user => user.uid === uid); 

      if (user) {
        return res.status(200).json({ 
          user: { 
            ...user.toJSON(),
            displayName: user.displayName || 'Sin nombre' // Añadimos displayName
          } 
        }); 
      } else {
        return res.status(404).json({ message: 'Usuario no encontrado' });
      }
    }

    while (result.pageToken) {
      result = await admin.auth().listUsers(1000, result.pageToken);
      userRecords.push(...result.users);
    }

    res.status(200).json({ 
      users: userRecords.map(user => ({
        ...user.toJSON(),
        displayName: user.displayName || 'Sin nombre' // Añadimos displayName
      }))
    });
  } catch (error) {
    res.status(500).json({ message: 'Error al obtener usuarios', error: error.message });
  }
});

// Eliminar usuario
router.delete('/deleteUser/:uid', async (req, res) => {
  const { uid } = req.params;  

  try {
    const userRecord = await admin.auth().getUser(uid); // Obtener datos del usuario
    await admin.auth().deleteUser(uid);

    res.status(200).json({ 
      message: `Usuario con UID ${uid} eliminado exitosamente`,
      displayName: userRecord.displayName || 'Sin nombre' // Usamos displayName de Firebase
    });
  } catch (error) {
    res.status(500).json({ message: 'Error al eliminar el usuario', error: error.message });
  }
});

// Crear usuario
router.post('/createUser', async (req, res) => {
  const { email, password, displayName, photoURL, disabled } = req.body;

  // Validación de displayName obligatorio
  if (!displayName) {
    return res.status(400).json({ message: 'El campo displayName es obligatorio' });
  }

  try {
    const userRecord = await admin.auth().createUser({
      email,
      password,
      displayName,  // Usamos el campo displayName
      photoURL,
      disabled: disabled || false, 
    });

    res.status(201).json({
      message: `Usuario creado exitosamente`,
      user: { 
        ...userRecord.toJSON(),
        displayName: displayName // Usamos displayName al devolver la respuesta
      },
    });
  } catch (error) {
    res.status(500).json({ message: 'Error al crear el usuario', error: error.message });
  }
});

// Editar correo y contraseña
router.put('/updateUser/:uid', async (req, res) => {
  const { uid } = req.params;  
  const { email, password, displayName } = req.body;  

  // Validación de displayName obligatorio
  if (!displayName) {
    return res.status(400).json({ message: 'El campo displayName es obligatorio' });
  }

  try {
    const updates = {};
    if (email) updates.email = email;
    if (password) updates.password = password;
    updates.displayName = displayName;  // Siempre actualizamos displayName porque es obligatorio

    const updatedUser = await admin.auth().updateUser(uid, updates);

    res.status(200).json({
      message: `Usuario con UID ${uid} actualizado exitosamente`,
      user: { 
        ...updatedUser.toJSON(),
        displayName: updatedUser.displayName // Retornamos el displayName actualizado
      },
    });
  } catch (error) {
    res.status(500).json({ message: 'Error al actualizar el usuario', error: error.message });
  }
});

export default router;

