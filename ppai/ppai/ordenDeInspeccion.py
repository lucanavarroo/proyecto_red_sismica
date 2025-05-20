from estado import Estado
class OrdenDeInspeccion:
    def __init__(self, numero_orden, fecha_inicio, fechaHoraFinalizacion=None, estado: Estado = Estado("OI","Pendiente")):
        self.numeroOrden = numero_orden
        self.fechaInicio = fecha_inicio
        self.fechaHoraFinalizacion = fechaHoraFinalizacion
        self.estado = estado

    def esta_completamente_realizada(self):
        return self.estado == "Completamente Realizada"
    
    def set_fecha_fin(self, fecha_fin):
        self.fecha_fin = fecha_fin
        self.estado = "Cerrada"
