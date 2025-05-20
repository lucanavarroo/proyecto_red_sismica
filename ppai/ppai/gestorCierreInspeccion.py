from datetime import datetime
from ordenDeInspeccion import OrdenDeInspeccion
from pantalla_ccrs import PantallaCCRS
from interfazNotificacionMail import InterfazNotificacionMail
from sismografo import Sismografo
from empleado import Empleado
from typing import List, Tuple

class GestorCierreInspeccion:   
    def __init__(self, empleado_logueado, fecha_actual, mail, sesion_actual):
        self.empleado_logueado = empleado_logueado
        self.fecha_actual = fecha_actual
        self.mail = mail
        self.sesion_actual = sesion_actual
        self.ordenes = []  # Lista de órdenes que el gestor puede manipular
        self.motivos = []  # Lista de tuplas (motivo, comentario)
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

    def tomar_seleccion_motivos(self, motivos_comentarios: List[Tuple[str, str]]):
        self.motivos = motivos_comentarios

    def solicitar_confirmacion_cierre(self, orden_id):
        orden = self.buscar_orden(orden_id)
        if orden:
            print(f"Solicitando confirmación de cierre para la orden {orden.numero_orden}")
        else:
            print("Orden no encontrada para confirmación.")

    def confirmar_cierre(self, orden_id):
        orden = self.buscar_orden(orden_id)
        if orden and orden.esta_completamente_realizada():
            # Establecer la fecha de finalización de la orden
            orden.set_fecha_fin(self.fecha_actual)

            # Cambiar estado del sismógrafo
            sismografo = Sismografo(id="S1", estado="Operativo")  # Aquí deberías cargar el real desde DB
            sismografo.poner_fuera_de_servicio(self.motivos, self.fecha_actual)

            # Publicar en pantalla de la CCRS
            PantallaCCRS().publicar()

            # Enviar notificaciones a los responsables
            responsables = [
                Empleado("Carlos", "Pérez", "carlos@ejemplo.com"),
                Empleado("Ana", "López", "ana@ejemplo.com")
            ]
            for responsable in responsables:
                InterfazNotificacionMail().enviar_mail(
                    responsable.mail,
                    "Cierre de Inspección",
                    f"Sismógrafo {sismografo.id} fuera de servicio desde {self.fecha_actual.strftime('%Y-%m-%d %H:%M')}.\n"
                    f"Motivos: {self.motivos}\n"
                    f"Observación: {self.observacion_cierre}"
                )
            print(f"Orden {orden.numero_orden} cerrada correctamente.")
        else:
            print("No se puede cerrar la orden. No está completamente realizada o no se encontró.")

# --- Ejemplo de uso para pruebas ---
if __name__ == "__main__":
    from datetime import datetime
    gestor = GestorCierreInspeccion(
        empleado_logueado="Juan Pérez",
        fecha_actual=datetime.now(),
        mail="juan@empresa.com",
        sesion_actual="SESION123"
    )

    # Crear orden simulada con fecha_inicio actual y estado "Completamente Realizada"
    orden_simulada = OrdenDeInspeccion(
        numero_orden="123",
        fecha_inicio=datetime.now(),
        estado="Completamente Realizada"
    )
    gestor.ordenes.append(orden_simulada)

    # Simular ingreso de observación y motivos
    gestor.ingresar_observacion_cierre("Observación de prueba para cierre.")
    gestor.tomar_seleccion_motivos([
        ("Falla eléctrica", "Cortocircuito detectado"),
        ("Daño físico", "Rotura en carcasa")
    ])

    # Confirmar cierre de orden
    gestor.confirmar_cierre("123")
