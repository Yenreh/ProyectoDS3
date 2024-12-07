import { useEffect } from 'react';
import { getTimeCommunication } from '../api/apis';  // Asegúrate de importar la función correctament
const ComunicacionTiempoReal = () => {
  // Llama a la función que obtiene los datos al montar el componente
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getTimeCommunication();  // Realiza la solicitud GET
        console.log('Datos obtenidos:', response);  // Maneja los datos (puedes hacer lo que necesites con ellos)
      } catch (error) {
        console.error('Error al obtener los datos:', error.message);  // Maneja el error
      }
    };

    fetchData();  // Llama a la función cuando el componente se monta
  }, []);  // Solo se ejecuta una vez cuando el componente se monta

  return null;  // No se muestra nada en la UI
};

export default ComunicacionTiempoReal;
