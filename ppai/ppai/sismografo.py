from estado import Estado
from cambioDeEstado import CambioDeEstado
from datetime import date
class Sismografo:
    def __init__(self, fechaAdquisicion: date ,identificadorSismografo: str, nroSerie: int , estadoActual:Estado, cambiosEstado: CambioDeEstado = None):
        if cambiosEstado is None:
            self.cambiosEstado = []
        else:
            self.cambiosEstado = cambiosEstado
        self.fechaAdquisicion = fechaAdquisicion
        self.identificadorSismografo = identificadorSismografo
        self.nroSerie = nroSerie
        self.estadoActual = estadoActual
        self.cambiosEstado = cambiosEstado

    def getIdentificadorSismografo(self):
        return self.identificadorSismografo

    def setEstadoActual(self, estadoActual: Estado):
        self.estadoActual = estadoActual
        
    def crearCambioEstado(self, fechaCambio: date, estado: Estado, responsableInspeccion, motivoFueraServicio: str, fechaHoraInicio: date, fechaHoraFin: date):
        cambio = CambioDeEstado(estado,responsableInspeccion,fechaHoraInicio, motivoFueraServicio, fechaHoraFin)
        self.cambiosEstado.append(cambio)

    def cerrarServicio(self):
        #ESTE HAY QUE DEFINIRLO AL FINAL PORQUE ES COMPLEJO PRIMERO TIENEN QUE ESTAR TODOS LOS DEMAS
        pass