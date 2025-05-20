from datetime import datetime
from ordenDeInspeccion import OrdenDeInspeccion
from pantallaCCRS import PantallaCCRS
from interfazNotificacionMail import InterfazNotificacionMail
from empleado import Empleado
from sesion import Sesion
from interfazCierreInspeccion import InterfazCierreInspeccion
from usuario import Usuario
from estado import Estado

class GestorCierreInspeccion:   
    def __init__(self,
        mails=None,
        observacionCierre="",
        pantallaCierreInspeccion: InterfazCierreInspeccion = None,
        listSeleccionMotivo=None,
        listComentarioParaMotivo=None,
        estadoCerrado: Estado = None,
        listMotivoTipo=None,
        listMailsResponsables=None,
        observacionOrdenCierre="",
        ordenInspeccionSeleccionada: OrdenDeInspeccion = None,
        estadoCompletamenteRealizado: Estado = None,
        listOrdenesInspeccion=None,
        pantallaCCRS: PantallaCCRS = None,
        usuarioLogueado: Usuario = None,
        pantallaMail: InterfazNotificacionMail = None,
        sesionActual: Sesion = None, 
        empleadoLogueado: Empleado = None,
        fechaHoraActual: datetime = None
    ):
        self.mails = mails or []
        self.observacionCierre = observacionCierre
        self.sesionActual = sesionActual
        self.empleadoLogueado = empleadoLogueado
        self.fechaHoraActual = fechaHoraActual or datetime.now()
        self.pantallaCierreInspeccion = pantallaCierreInspeccion
        self.pantallaMail = pantallaMail
        self.pantallaCCRS = pantallaCCRS
        self.usuarioLogueado = usuarioLogueado
        self.listOrdenesInspeccion = listOrdenesInspeccion or []
        self.estadoCompletamenteRealizado = estadoCompletamenteRealizado or Estado("OI", "Completamente Realizado")
        self.ordenInspeccionSeleccionada = ordenInspeccionSeleccionada
        self.observacionOrdenCierre = observacionOrdenCierre
        self.listSeleccionMotivo = listSeleccionMotivo or []
        self.listComentarioParaMotivo = listComentarioParaMotivo or []
        self.estadoCerrado = estadoCerrado or Estado("OI", "Cerrada")
        self.estadoFueraDeServicio = Estado("Sismografo", "Fuera de Servicio")
        self.listMotivoTipo = listMotivoTipo or []
        self.listMailsResponsables = listMailsResponsables or []

    def buscarRILogueado(self):
        if self.sesionActual:
            self.usuarioLogueado = self.sesionActual.obtenerRILogueado()

    def buscarRolDeRI(self):
        if self.usuarioLogueado:
            return self.usuarioLogueado.getRol()
        return None

    def ordenarPorFechaDefFin(self):
        if self.listOrdenesInspeccion:
            self.listOrdenesInspeccion.sort(key=lambda oi: oi.getFechaFinalizacion() or datetime.max)

    def tomarOISeleccionada(self, ordenSeleccionada: OrdenDeInspeccion):
        if ordenSeleccionada is not None:
            self.ordenInspeccionSeleccionada = ordenSeleccionada

    def pedirObservacionOrdenCierre(self):
        if self.pantallaCierreInspeccion:
            self.observacionCierre = self.pantallaCierreInspeccion.pedirObservacionOrdenCierre()

    def tomarObsOrdenCierre(self, observacion=None):
        if observacion is not None:
            self.observacionCierre = observacion

    def tomarSeleccionMotivo(self, motivoSeleccionado):
        self.listSeleccionMotivo.append(motivoSeleccionado)

    def tomarComentario(self, comentario):
        self.listComentarioParaMotivo.append(comentario)

    def iniciarCierre(self):
        self.ordenInspeccionSeleccionada = None
        self.observacionCierre = ""
        self.listSeleccionMotivo = []
        self.listComentarioParaMotivo = []

    def obtenerConfirmacionOI(self):
        if self.pantallaCierreInspeccion and self.ordenInspeccionSeleccionada:
            return self.pantallaCierreInspeccion.solicitar_confirmacion_cierre(self.ordenInspeccionSeleccionada)
        return False

    def tomarConfirmacionCierreOI(self, confirmado=False):
        if confirmado:
            self.cerrarOI()

    def validarDatosMinimosRequeridos(self):
        # Ahora valida también que haya al menos un motivo seleccionado y observación no vacía
        return (
            self.ordenInspeccionSeleccionada is not None and
            bool(self.observacionCierre) and
            len(self.listSeleccionMotivo) > 0
        )

    def cerrarOI(self):
        if self.validarDatosMinimosRequeridos():
            self.ordenInspeccionSeleccionada.setEstado(self.estadoCerrado)
            self.ordenInspeccionSeleccionada.setObservacionCierre(self.observacionCierre)
            self.ordenInspeccionSeleccionada.setFechaHoraCierre(self.getFechaHoraActual())
            self.actualizarSismografo()
            self.enviarNotificacionesPorMail()
            self.publicarEnMonitores()
            self.finCU()
        else:
            print("Error: Faltan datos mínimos para cerrar la orden (motivo y observación obligatorios).")

    def actualizarSismografo(self):
        if self.ordenInspeccionSeleccionada:
            estacion = self.ordenInspeccionSeleccionada.getEstacionSismologica()
            if estacion and hasattr(estacion, "sismografo") and estacion.sismografo:
                if hasattr(estacion.sismografo, "setEstadoActual"):
                    estacion.sismografo.setEstadoActual(self.estadoCerrado)
                else:
                    print("Advertencia: El sismógrafo no tiene el método setEstadoActual.")

    def habilitarActualizarSismografo(self):
        """
        Habilita la actualización del sismógrafo si la orden seleccionada está cerrada.
        """
        if self.ordenInspeccionSeleccionada and self.ordenInspeccionSeleccionada.getEstado() == self.estadoCerrado:
            estacion = self.ordenInspeccionSeleccionada.getEstacionSismologica()
            if estacion and hasattr(estacion, "sismografo") and estacion.sismografo:
                if hasattr(estacion.sismografo, "habilitarActualizacion"):
                    estacion.sismografo.habilitarActualizacion()
                    return True
                else:
                    print("Advertencia: El sismógrafo no tiene el método habilitarActualizacion.")
        return False