from estado import Estado
from estacionSismologica import EstacionSismologica

class OrdenDeInspeccion:
    def __init__(
        self,
        numeroOrden,
        fechaHoraInicio,
        fechaHoraFinalizacion=None,
        fechaHoraCierre=None,
        observacionCierre=None,
        estado: Estado = Estado("OI", "Pendiente"),
        estacionSismologica: EstacionSismologica = None
    ):
        self.numeroOrden = numeroOrden
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFinalizacion = fechaHoraFinalizacion
        self.fechaHoraCierre = fechaHoraCierre
        self.observacionCierre = observacionCierre
        self.estado = estado
        self.estacionSismologica = estacionSismologica

    def getNumeroOrden(self):
        return self.numeroOrden

    def getFechaHoraInicio(self):
        return self.fechaHoraInicio

    def getFechaHoraFinalizacion(self):
        return self.fechaHoraFinalizacion

    def getFechaHoraCierre(self):
        return self.fechaHoraCierre

    def getObservacionCierre(self):
        return self.observacionCierre

    def getEstado(self):
        return self.estado

    def getEstacionSismologica(self):
        return self.estacionSismologica

    def setNumeroOrden(self, numeroOrden):
        self.numeroOrden = numeroOrden

    def setFechaHoraInicio(self, fechaHoraInicio):
        self.fechaHoraInicio = fechaHoraInicio

    def setFechaHoraFinalizacion(self, fechaHoraFinalizacion):
        self.fechaHoraFinalizacion = fechaHoraFinalizacion

    def setFechaHoraCierre(self, fechaHoraCierre):
        self.fechaHoraCierre = fechaHoraCierre

    def setObservacionCierre(self, observacionCierre):
        self.observacionCierre = observacionCierre

    def setEstado(self, estado: Estado):
        self.estado = estado

    def setEstacionSismologica(self, estacionSismologica: EstacionSismologica):
        self.estacionSismologica = estacionSismologica

