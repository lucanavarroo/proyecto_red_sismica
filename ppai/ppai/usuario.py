from empleado import Empleado

class Usuario:
    def __init__(self, nombre_usuario: str, contrasena: str, empleado: Empleado):
        self.nombreUsuario = nombre_usuario
        self.contrasena = contrasena
        self.empleado = empleado

    def getEmpleado(self):
        return self.empleado
    def getNombreUsuario(self):
        return self.nombreUsuario
    def setEmpleado(self, empleado: Empleado):
        self.empleado = empleado
    def setNombreUsuario(self, nombre_usuario: str):
        self.nombreUsuario = nombre_usuario