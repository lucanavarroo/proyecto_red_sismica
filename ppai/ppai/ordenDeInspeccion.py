class OrdenDeInspeccion:
    def __init__(self, numero_orden, fecha_inicio, fecha_fin=None, estado="Pendiente"):
        self.numero_orden = numero_orden
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado

    def esta_completamente_realizada(self):
        return self.estado == "Completamente Realizada"
    
    def set_fecha_fin(self, fecha_fin):
        self.fecha_fin = fecha_fin
        self.estado = "Cerrada"
