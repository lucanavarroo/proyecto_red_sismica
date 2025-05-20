from rol import Rol

class Empleado:
    def __init__(self, nombre: str, apellido: str, mail: str, telefono: str, rol: Rol):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.telefono = telefono
        self.rol = rol

    def esResponsableDeReparacion(self):
        return self.rol.sosResponsableDeReparacion()
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getMail(self):
        return self.mail
    def getTelefono(self):
        return self.telefono
    def getRol(self):
        return self.rol
    def setNombre(self, nombre: str):
        self.nombre = nombre
    def setApellido(self, apellido: str):
        self.apellido = apellido
    def setMail(self, mail: str):
        self.mail = mail
    def setTelefono(self, telefono: str):
        self.telefono = telefono
    def setRol(self, rol: Rol):
        self.rol = rol
    def obtenerMail(self):
        return self.getMail()