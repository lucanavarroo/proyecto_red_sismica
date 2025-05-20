class Estado:
    def __init__(self, ambito: str, nombreEstado: str):
        self.ambito = ambito
        self.nombreEstado = nombreEstado

    def __str__(self):
        return f"Estado(nombreEstado={self.nombreEstado}, ambito={self.ambito})"
    
    def sosCompletamenteRealizado(self):
        return self.nombreEstado.lower() == "completamente realizado"
    
    def sosCompletamenteRechazado(self):
        return self.nombreEstado.lower() == "completamente rechazado"

    def sosCerrada(self):
        return self.nombreEstado.lower() == "cerrada"

    def sosFueraDeServicio(self):
        return self.nombreEstado.lower() == "fuera de servicio"

    def sosAmbitoOI(self):
        return self.ambito.lower() == "oi"

    def sosAmbitoSismografo(self):
        return self.ambito.lower() == "sismografo"
