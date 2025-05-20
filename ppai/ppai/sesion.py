from datetime import datetime

class Sesion:
    def __init__(self, usuario, fecha_hora_inicio: datetime, fecha_hora_fin: datetime = None):
        self.usuario = usuario
        self.fecha_hora_inicio = fecha_hora_inicio
        self.fecha_hora_fin = fecha_hora_fin

    def obtenerRILogueado(self):
        return self.usuario.nombreUsuario