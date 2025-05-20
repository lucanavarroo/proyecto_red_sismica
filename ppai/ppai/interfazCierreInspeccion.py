class InterfazCierreInspeccion:
    def __init__(
        self,
        botonCancelarCierre=None,
        botonConfirmarCierre=None,
        grillaOrdenInspeccionFinalizadas=None,
        grillaOrdenInspeccionSelec=None,
        ordenInspeccionSeleccionada=None,
        gestor=None
    ):
        self.botonCancelarCierre = botonCancelarCierre
        self.botonConfirmarCierre = botonConfirmarCierre
        self.grillaOrdenInspeccionFinalizadas = grillaOrdenInspeccionFinalizadas
        self.grillaOrdenInspeccionSelec = grillaOrdenInspeccionSelec
        self.ordenInspeccionSeleccionada = ordenInspeccionSeleccionada
        self.gestor = gestor

    def boton_cancelar_cierre(self):
        """Cancela el proceso de cierre de inspección."""
        print("Cierre de inspección cancelado.")
        self.gestor.iniciarCierre()

    def boton_confirmar_cierre(self):
        """Confirma el cierre de la inspección."""
        print("Confirmando cierre de inspección...")
        self.confirmar_cierre()

    def grilla_ordenes_seleccionadas(self):
        """Devuelve las órdenes seleccionadas en la grilla."""
        if self.grillaOrdenInspeccionSelec:
            return self.grillaOrdenInspeccionSelec.obtener_seleccionadas()
        return []

    def ingresar_observacion_cierre(self, texto):
        """Registra una observación en el proceso de cierre."""
        print(f"Observación ingresada: {texto}")
        self.gestor.tomarObsOrdenCierre(texto)

    def seleccionar_motivo(self, motivo):
        """Selecciona el motivo del cierre de inspección."""
        print(f"Motivo seleccionado: {motivo}")
        self.gestor.tomarSeleccionMotivo(motivo)

    def ingresar_comentario(self, comentario):
        """Registra un comentario para el motivo seleccionado."""
        print(f"Comentario ingresado: {comentario}")
        self.gestor.tomarComentario(comentario)

    def pedirObservacionOrdenCierre(self):
        """Solicita al usuario que ingrese una observación de cierre."""
        texto = input("Ingrese la observación de cierre: ")
        self.ingresar_observacion_cierre(texto)

    def solicitar_confirmacion_cierre(self, orden_id):
        """Solicita la confirmación de cierre para una orden específica."""
        print(f"Solicitando confirmación de cierre para orden {orden_id}...")
        self.ordenInspeccionSeleccionada = orden_id
        return self.gestor.obtenerConfirmacionOI()

    def confirmar_cierre(self):
        """Ejecuta el cierre de la inspección."""
        if self.ordenInspeccionSeleccionada:
            print(f"Cerrando inspección para orden {self.ordenInspeccionSeleccionada}...")
            self.gestor.tomarConfirmacionCierreOI(True)
            self.refrescar_grilla_finalizadas()
            self.mostrar_mensaje("Inspección cerrada correctamente.")
        else:
            print("No hay orden de inspección seleccionada.")
            self.mostrar_mensaje("Debe seleccionar una orden para cerrar.")

    def refrescar_grilla_finalizadas(self):
        """Actualiza la grilla de órdenes finalizadas."""
        print("Grilla de órdenes finalizadas actualizada.")
        # Aquí deberías actualizar la UI real si corresponde

    def mostrar_mensaje(self, mensaje):
        """Muestra un mensaje al usuario."""
        print(f"Mensaje: {mensaje}")