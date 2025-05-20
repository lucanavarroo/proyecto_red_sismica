from estado import Estado
from cambioDeEstado import CambioDeEstado
from datetime import date

class Sismografo:
    def __init__(self, fechaAdquisicion: date, identificadorSismografo: str, nroSerie: int, estadoActual: Estado, cambiosEstado=None):
        self.fechaAdquisicion = fechaAdquisicion
        self.identificadorSismografo = identificadorSismografo
        self.nroSerie = nroSerie
        self.estadoActual = estadoActual
        if cambiosEstado is None:
            self.cambiosEstado = []
        else:
            self.cambiosEstado = cambiosEstado

    def getIdentificadorSismografo(self):
        return self.identificadorSismografo

    def setEstadoActual(self, estadoActual: Estado):
        self.estadoActual = estadoActual

    def crearCambioEstado(self, fechaCambio: date, estado: Estado, responsableInspeccion, motivoFueraServicio: str, fechaHoraInicio: date, fechaHoraFin: date):
        cambio = CambioDeEstado(estado, responsableInspeccion, fechaHoraInicio, motivoFueraServicio, fechaHoraFin)
        self.cambiosEstado.append(cambio)

    def habilitarActualizacion(self):
        print("Actualización del sismógrafo habilitada.")

    def cerrarServicio(self, responsableInspeccion, motivoFueraServicio: str, fechaHoraInicio: date, fechaHoraFin: date = None):
        """
        Cambia el estado del sismógrafo a 'Fuera de Servicio' y registra el cambio.
        """
        estado_fuera_servicio = Estado("Sismografo", "Fuera de Servicio")
        self.setEstadoActual(estado_fuera_servicio)
        self.crearCambioEstado(
            fechaCambio=fechaHoraInicio,
            estado=estado_fuera_servicio,
            responsableInspeccion=responsableInspeccion,
            motivoFueraServicio=motivoFueraServicio,
            fechaHoraInicio=fechaHoraInicio,
            fechaHoraFin=fechaHoraFin
        )