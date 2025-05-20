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
        # Valida que haya una orden seleccionada, observación y al menos un motivo
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
        if self.ordenInspeccionSeleccionada:
            estado_actual = self.ordenInspeccionSeleccionada.getEstado()
            # Compara por nombre si __eq__ no está implementado
            if hasattr(estado_actual, "nombreEstado") and hasattr(self.estadoCerrado, "nombreEstado"):
                estados_iguales = estado_actual.nombreEstado == self.estadoCerrado.nombreEstado
            else:
                estados_iguales = estado_actual == self.estadoCerrado

            if estados_iguales:
                estacion = self.ordenInspeccionSeleccionada.getEstacionSismologica()
                if estacion and hasattr(estacion, "sismografo") and estacion.sismografo:
                    if hasattr(estacion.sismografo, "habilitarActualizacion"):
                        estacion.sismografo.habilitarActualizacion()
                        return True
                    else:
                        print("Advertencia: El sismógrafo no tiene el método habilitarActualizacion.")
        return False

    def getFechaHoraActual(self):
        return datetime.now()

    def enviarNotificacionesPorMail(self):
        mails = self.listMailsResponsables if self.listMailsResponsables else []
        for mail in mails:
            if self.pantallaMail:
                self.pantallaMail.enviar_mail(mail, "Cierre de Inspección", "La orden ha sido cerrada.")

    def publicarEnMonitores(self):
        if self.pantallaCCRS and self.ordenInspeccionSeleccionada:
            self.pantallaCCRS.publicar_cierre(self.ordenInspeccionSeleccionada)

    def finCU(self):
        self.ordenInspeccionSeleccionada = None
        self.observacionCierre = ""
        self.listSeleccionMotivo = []
        self.listComentarioParaMotivo = []

    # Métodos auxiliares para integración con Flask o UI
    def buscar_orden(self, orden_id):
        for orden in self.listOrdenesInspeccion:
            if hasattr(orden, "id") and str(orden.id) == str(orden_id):
                return orden
        return None

    def ingresarObservacionCierre(self, observacion):
        self.tomarObsOrdenCierre(observacion)

    def tomarSeleccionMotivos(self, motivos):
        self.listSeleccionMotivo.clear()
        self.listComentarioParaMotivo.clear()
        for motivo, comentario in motivos:
            self.tomarSeleccionMotivo(motivo)
            self.tomarComentario(comentario)

    def confirmarCierre(self, orden_id):
        orden = self.buscar_orden(orden_id)
        if orden:
            self.ordenInspeccionSeleccionada = orden
            self.cerrarOI()