from datetime import datetime
class HistoriaClinica:
    """Representa una entrada en la historia clínica de un paciente."""
    def __init__(self, nombre_paciente: str, tratamiento: str, costo: float, fecha: str):
        self.nombre_paciente = nombre_paciente
        self.tratamiento = tratamiento
        self.costo = costo
        self.fecha = fecha  # Fecha en formato string, puede validarse con datetime si se desea

    def __str__(self):
        return f"Paciente: {self.nombre_paciente} | Tratamiento: {self.tratamiento} | Costo: ${self.costo:.2f} | Fecha: {self.fecha}"
class Paciente:
    """Representa a un paciente con su historial clínico."""
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.historial = []  # Lista de objetos HistoriaClinica
    def agregar_historia_clinica(self, tratamiento: str, costo: float, fecha: str):
        """Agrega una nueva entrada al historial clínico del paciente."""
        nueva_historia = HistoriaClinica(self.nombre, tratamiento, costo, fecha)
        self.historial.append(nueva_historia)
    def obtener_historial(self):
        """Devuelve el historial clínico completo del paciente."""
        return self.historial
    def __str__(self):
        if not self.historial:
            return f"{self.nombre} no tiene historial clínico."
        historial_str = "\n".join(str(historia) for historia in self.historial)
        return f"Historial clínico de {self.nombre}:\n{historial_str}"
