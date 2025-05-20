from datetime import datetime
from ordenDeInspeccion import OrdenDeInspeccion
from pantallaCCRS import PantallaCCRS
from interfazNotificacionMail import InterfazNotificacionMail
from sismografo import Sismografo
from empleado import Empleado
from typing import List, Tuple
from sesion import Sesion
from interfazCierreInspeccion import InterfazCierreInspeccion
from interfazNotificacionMail import InterfazNotificacionMail
from usuario import Usuario
from estado import Estado

class GestorCierreInspeccion:   
    def __init__(self,
    mails,
    observacionCierre,
    pantallaCierreInspeccion : InterfazCierreInspeccion,
    listSeleccionMotivo = None,
    listComentarioParaMotivo = None,
    estadoCerrado: Estado = None,
    listMotivoTipo = None,
    listMailsResponsables = None,
    observacionOrdenCierre = None,
    ordenInspeccionSeleccionada: OrdenDeInspeccion = None,
    estadoCompletamenteRealizado: Estado = None,
    listOrdenesInspeccion = None,
    pantallaCCRS: PantallaCCRS = None,
    usuarioLogueado: Usuario = None,
    pantallaMail: InterfazNotificacionMail = None,
    sesionActual: Sesion = None, 
    empleadoLogueado: Empleado = None,
    fechaHoraActual: datetime = datetime.now()):
        self.mails = mails
        self.observacionCierre = observacionCierre
        self.sesionActual = sesionActual
        self.empleadoLogueado = empleadoLogueado
        self.fechaHoraActual = fechaHoraActual
        self.pantallaCierreInspeccion = pantallaCierreInspeccion
        self.pantallaMail = pantallaMail
        self.pantallaCCRS = pantallaCCRS
        self.usuarioLogueado = usuarioLogueado
        self.listOrdenesInspeccion = listOrdenesInspeccion
        self.estadoCompletamenteRealizado = estadoCompletamenteRealizado
        self.ordenInspeccionSeleccionada = ordenInspeccionSeleccionada
        self.observacionOrdenCierre = observacionOrdenCierre
        self.listSeleccionMotivo = listSeleccionMotivo
        self.listComentarioParaMotivo = listComentarioParaMotivo
        self.estadoCerrado = estadoCerrado
        self.estadoFueraDeServicio = estadoCerrado
        self.listMotivoTipo = listMotivoTipo
        self.listMailsResponsables = listMailsResponsables
    

    def buscarRILogueado(self):
        self.usuarioLogueado = self.sesionActual.obtenerRILogueado()
        #es una clase empleado
    #def buscarOIdeRI(self, listaOrdenes):
        #listaEmpleado = []
        #for order in listaOrdenes:
            #if order.sosDeEmpleado():
                #if order.estado.sosCompletamenteRealizado():
                    #order.obtenerDatosOI()

                #listaEmpleado.append(order)
    
    def ordenarPorFechaDeFin(self):
        self.listOrdenesInspeccion.sort(key=lambda x: x.fechaFin, reverse=True)
  
    
    def tomarOISeleccionada(self, ordenInspeccionSeleccionada: OrdenDeInspeccion):
        self.ordenInspeccionSeleccionada = ordenInspeccionSeleccionada
    
    def pedirObservacionOrdenCierre(self):
        self.observacionOrdenCierre = self.pantallaCierreInspeccion.pedirObservacionOrdenCierre()
        
    

    def tomarObservacionOrdenCierre(self, observacionOrdenCierre: str):
        self.observacionOrdenCierre = observacionOrdenCierre
    
    



#comparacion#

    # Métodos del diagrama como stubs:
    def iniciarCierre(self): pass
    def buscarRILogueado(self): pass
    def buscarRolDeRI(self): pass
    def ordenarPorFechaDefFin(self): pass
    def pedirObservacionOrdenCierre(self): pass
    def tomarObsOrdenCierre(self): pass
    def tomarOISeleccionada(self): pass
    def tomarSeleccionMotivo(self): pass
    def tomarComentario(self): pass
    def obtenerConfirmacionOI(self): pass
    def tomarConfirmacionCierreOI(self): pass
    def validarDatosMinimosRequeridos(self): pass
    def cerrarOI(self): pass
    def getFechaHoraActual(self): pass
    def actualizarSismografo(self): pass
    def obtenerMailsResponsablesReparacion(self): pass
    def enviarNotificacionesPorMail(self): pass
    def publicarEnMonitores(self): pass
    def habilitarActualizarSismografo(self): pass
    def finCU(self): pass
    