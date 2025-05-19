class Estado:
    def __init__(self, ambito: str, nombre_estado: str):
        self.ambito = ambito
        self.nombre_estado = nombre_estado

    def es_completamente_rechazado(self) -> bool:
        return self.nombre_estado.lower() == "rechazado"