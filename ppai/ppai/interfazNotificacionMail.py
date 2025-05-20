class InterfazNotificacionMail:
    def enviar_mail(self, destinatario, asunto, mensaje):
        print(f"Enviando mail a {destinatario} - Asunto: {asunto} - Mensaje: {mensaje}")