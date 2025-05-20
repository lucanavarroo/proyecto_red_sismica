from datetime import datetime
from usuario import Usuario

class Sesion:
    def __init__(self, usuario: Usuario, fechaHoraInicio: datetime, fechaHoraFin: datetime = None):
        self.usuario = usuario
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin

    def obtenerRILogueado(self):
        return self.usuario.getEmpleado()