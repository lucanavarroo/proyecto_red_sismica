from datetime import datetime
from orden_de_inspeccion import OrdenDeInspeccion
from pantalla_ccrs import PantallaCCRS
from interfaz_notificacion_mail import InterfazNotificacionMail

class GestorCierreInspeccion:
    def __init__(self, empleado_logueado, fecha_actual, mail, sesion_actual):
        self.empleado_logueado = empleado_logueado
        self.fecha_actual = fecha_actual
        self.mail = mail
        self.sesion_actual = sesion_actual
        self.ordenes = []
        self.motivo = None
        self.observacion_cierre = ""

    def iniciar_cierre(self):
        print("Inicio de cierre iniciado.")

    def buscar_orden(self, orden_id):
        for orden in self.ordenes:
            if orden.numero_orden == orden_id:
                return orden
        return None

    def ingresar_observacion_cierre(self, texto):
        self.observacion_cierre = texto

    def tomar_seleccion_motivo(self, motivo):
        self.motivo = motivo

    def solicitar_confirmacion_cierre(self, orden_id):
        orden = self.buscar_orden(orden_id)
        if orden:
            print(f"Solicitando confirmación de cierre para la orden {orden.numero_orden}")

    def confirmar_cierre(self, orden_id):
        orden = self.buscar_orden(orden_id)
        if orden:
            orden.set_fecha_fin(self.fecha_actual)
            PantallaCCRS().publicar()
            InterfazNotificacionMail().enviar_mail(self.mail, "Cierre Confirmado", f"Orden {orden.numero_orden} cerrada.")