class Sismografo:
    def __init__(self, id, estado):
        self.id = id
        self.estado = estado
        self.motivos_fuera_servicio = []

    def poner_fuera_de_servicio(self, motivos, fecha):
        self.estado = "Fuera de Servicio"
        self.motivos_fuera_servicio = motivos
        self.fecha_fuera_servicio = fecha
