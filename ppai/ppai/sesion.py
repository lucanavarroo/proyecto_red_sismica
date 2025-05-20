from datetime import datetime

class Sesion:
    def __init__(self, fecha_hora_inicio: datetime, fecha_hora_fin: datetime = None):
        self.fecha_hora_inicio = fecha_hora_inicio
        self.fecha_hora_fin = fecha_hora_fin

    def obtener_rl_logueado(self):
        return "Responsable Logueado"