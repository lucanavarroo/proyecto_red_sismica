class Rol:
    def __init__(self, name: str, description: str):
        self.nombre = name
        self.descripcionRol = description

    def __str__(self):
        return f"Rol(name={self.name}, description={self.description})"

    def getNombreRol(self):
        return self.nombre

    def getDescripcionRol(self):
        return self.descripcionRol

    def setNombreRol(self, nombre: str):
        self.nombre = nombre

    def setDescripcionRol(self, descripcion: str):
        self.descripcionRol = descripcion

    def sosResponsableReparacion(self):
        if self.nombre == "Responsable de Reparacion":
            return True
        else:
            return False