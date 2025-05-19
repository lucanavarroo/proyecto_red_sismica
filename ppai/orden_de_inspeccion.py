class OrdenDeInspeccion:
    def __init__(self, numero_orden, fecha_inicio, fecha_fin=None):
        self.numero_orden = numero_orden
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def get_fecha_finalizacion(self):
        return self.fecha_fin

    def set_estado(self, estado):
        self.estado = estado

    def set_fecha_fin(self, fecha):
        self.fecha_fin = fecha