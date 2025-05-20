class Rol:
    def __init__(self, nombre: str, descripcionRol: str):
        self.nombre = nombre
        self.descripcionRol = descripcionRol

    def __str__(self):
        return f"Rol(nombre={self.nombre}, descripcion={self.descripcionRol})"

    def getNombreRol(self):
        return self.nombre

    def getDescripcionRol(self):
        return self.descripcionRol

    def setNombreRol(self, nombre: str):
        self.nombre = nombre

    def setDescripcionRol(self, descripcion: str):
        self.descripcionRol = descripcion

    def sosResponsableDeReparacion(self):
        return self.nombre.lower() == "responsable de reparacion"