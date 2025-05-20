from datetime import datetime

class CambioDeEstado:
    def __init__(self, fecha_hora_inicio: datetime, fecha_hora_fin: datetime = None):
        self.fecha_hora_inicio = fecha_hora_inicio
        self.fecha_hora_fin = fecha_hora_fin

    def es_actual(self) -> bool:
        return self.fecha_hora_fin is None

    def set_fecha_hora_fin(self, fecha: datetime):
        self.fecha_hora_fin = fecha