import "../styles/users.css"

const appointments = [
    { patient: "Dylan Farkas", doctor: "Javier Lasso", dateTime: "2024-12-15 15:00:00", status: "PENDING" },
    { patient: "Ervin Carabali", doctor: "Manuel Medina", dateTime: "2025-01-10 12:00:00", status: "PENDING" },
    { patient: "Herney Quintero", doctor: "Fredy Ballesteros", dateTime: "2025-05-10 5:00:00", status: "PENDING" },
    { patient: "Wilson Mosquera", doctor: "Fredy Ballesteros", dateTime: "2025-05-10 5:00:00", status: "CANCELLED" },
];

const AppointmentTable = () => {
    return (
        <div className="container" style={{ maxWidth: "100%" }}>

            {/* Tabla de Appointments */}
            <div className="table-responsive" style={{ maxHeight: "480px", overflowY: "auto" }}>
                <table className="table table-bordered">
                    <thead>
                        <tr>
                            <th>Paciente</th>
                            <th>Médico</th>
                            <th>Fecha y Hora</th>
                            <th>Estado</th>
                            <th colSpan="2">Opciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {appointments.map((appointment, index) => (
                            <tr key={index}>
                                <td>{appointment.patient}</td>
                                <td>{appointment.doctor}</td>
                                <td>{appointment.dateTime}</td>
                                <td>{appointment.status}</td>
                                <td>
                                    <button className="bg-blue-500 hover:bg-blue-400 text-white font-bold py-2 px-4 border-b-4 border-blue-700 hover:border-blue-500 rounded">Editar</button>
                                </td>
                                <td>
                                    <button className="bg-red-500 hover:bg-red-400 text-white font-bold py-2 px-4 border-b-4 border-red-700 hover:border-red-500 rounded">Eliminar</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
            <button className="bg-green-500 hover:bg-green-400 text-white font-bold py-2 px-4 border-b-4 border-green-700 hover:border-green-500 rounded mt-5">
                Crear Cita
            </button>
        </div>
    );
};

export default AppointmentTable;
