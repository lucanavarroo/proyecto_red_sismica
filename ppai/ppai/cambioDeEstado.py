from datetime import datetime
from estado import Estado
from motivoFueraServicio import MotivoFueraServicio
from empleado import Empleado
from motivoTipo import MotivoTipo
class CambioDeEstado:
    def __init__(self, fecha_hora_inicio: datetime, estado: Estado ,empleado: Empleado , motivoFueraServicio: MotivoFueraServicio = [] ,fecha_hora_fin: datetime = None):
        self.fechaHoraInicio = fecha_hora_inicio
        self.fechaHoraFin = fecha_hora_fin
        self.estado = estado
        self.motivoFueraServicio = motivoFueraServicio
        self.empleado = empleado



    def esEstadoActual(self) -> bool:
        return self.fechaHoraFin is None
        
    def setFechaHoraFin(self, fecha_hora_fin: datetime):
        self.fechaHoraFin = fecha_hora_fin

    def crearMotivoFueraServicio(self, motivo: MotivoTipo, comentario: str):
        self.motivoFueraServicio.append(MotivoFueraServicio(motivo, comentario))
    