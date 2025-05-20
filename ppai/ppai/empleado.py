class Empleado:
    def __init__(self, nombre: str, apellido: str, mail: str):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail

    def es_responsable_de_reparacion(self):
        # Lógica que determina si el empleado es responsable
        return True