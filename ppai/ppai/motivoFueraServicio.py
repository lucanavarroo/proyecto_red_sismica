from motivoTipo import MotivoTipo

class MotivoFueraServicio:
    def __init__(self, comentario: str, motivo: MotivoTipo):
        self.comentario = comentario
        self.motivo = motivo

    def getComentario(self):
        return self.comentario
    def getMotivo(self):
        return self.motivo
    def setComentario(self, comentario: str):
        self.comentario = comentario
    def setMotivo(self, motivo: MotivoTipo):
        self.motivo = motivo