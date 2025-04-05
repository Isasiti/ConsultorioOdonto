class Cita:
    """Representa una cita agendada para un paciente."""
    contador_citas = 1  # Contador para generar números clave únicos
    def __init__(self, paciente: str, fecha: str, hora: str):
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
        self.numero_clave = f"{Cita.contador_citas:03d}"  # Genera clave con formato 001, 002, etc.
        self.realizada = False
        Cita.contador_citas += 1  # Incrementa el contador para la próxima cita
    def modificar_cita(self, nueva_fecha: str, nueva_hora: str):
        """Modifica la fecha y hora de la cita."""
        self.fecha = nueva_fecha
        self.hora = nueva_hora
    def cancelar_cita(self):
        """Cancela la cita marcándola como None."""
        self.paciente = None
        self.fecha = None
        self.hora = None
        self.numero_clave = None
    def marcar_como_realizada(self):
        """Marca la cita como realizada."""
        self.realizada = True
    def __str__(self):
        return f"Cita {self.numero_clave}: {self.paciente} - {self.fecha} a las {self.hora}"
class Agenda:
    """Gestiona las citas del consultorio."""
    def __init__(self):
        self.citas = [Cita]  # Lista de objetos Cita
    def agendar_cita(self, paciente: str, fecha: str, hora: str):
        """Crea una nueva cita y la agrega a la lista de citas."""
        nueva_cita = Cita(paciente, fecha, hora)
        self.citas.append(nueva_cita)
        return nueva_cita.numero_clave
    def listar_citas_pendientes(self):
        """Devuelve una lista con las citas pendientes."""
        return [cita for cita in self.citas if not cita.realizada]
    def buscar_cita(self, paciente: str):
        """Busca una cita por el nombre del paciente y devuelve su número clave."""
        for cita in self.citas:
            if cita.paciente == paciente:
                return cita.numero_clave
        return None  # Devuelve None si no se encuentra la cita
    def __str__(self):
        """Devuelve una representación en texto de todas las citas agendadas."""
        if not self.citas:
            return "No hay citas agendadas."
        return "\n".join(str(cita) for cita in self.citas)
