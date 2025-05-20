class Usuario:
    def __init__(self, nombre_usuario: str, contrasena: str, empleado):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.empleado = empleado

    def get_empleado(self):
        return self.empleado