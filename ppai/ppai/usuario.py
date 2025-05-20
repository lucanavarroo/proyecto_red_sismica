from empleado import Empleado
from rol import Rol

class Usuario:
    def __init__(self, nombreUsuario: str, contrasena: str, empleado: Empleado, rol: Rol):
        self.nombreUsuario = nombreUsuario
        self.contrasena = contrasena
        self.empleado = empleado
        self.rol = rol

    def getEmpleado(self):
        return self.empleado

    def getNombreUsuario(self):
        return self.nombreUsuario

    def setEmpleado(self, empleado: Empleado):
        self.empleado = empleado

    def setNombreUsuario(self, nombreUsuario: str):
        self.nombreUsuario = nombreUsuario

    def getRol(self):
        return self.rol

    def getRILogueado(self):
        return self.empleado