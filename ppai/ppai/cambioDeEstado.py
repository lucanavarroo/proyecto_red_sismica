from datetime import datetime
from estado import Estado
from motivoFueraServicio import MotivoFueraServicio
from empleado import Empleado
from motivoTipo import MotivoTipo

class CambioDeEstado:
    def __init__(self, estado: Estado, responsableInspeccion: Empleado, fechaHoraInicio: datetime = datetime.now(), motivoFueraServicio=None, fechaHoraFin: datetime = None):
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.estado = estado
        self.motivoFueraServicio = motivoFueraServicio if motivoFueraServicio is not None else []
        self.responsableInspeccion = responsableInspeccion

    def sosActual(self) -> bool:
        return (self.fechaHoraFin is None)
        
    def setFechaHoraFin(self, fechaHoraFin: datetime):
        self.fechaHoraFin = fechaHoraFin

    def crearMotivoFueraServicio(self, motivo: MotivoTipo, comentario: str):
        self.motivoFueraServicio.append(MotivoFueraServicio(comentario, motivo))

    # Métodos getters sugeridos
    def getEstado(self):
        return self.estado

    def getMotivoFueraServicio(self):
        return self.motivoFueraServicio

    def getResponsableInspeccion(self):
        return self.responsableInspeccion

    def getFechaHoraInicio(self):
        return self.fechaHoraInicio

    def getFechaHoraFin(self):
        return self.fechaHoraFin