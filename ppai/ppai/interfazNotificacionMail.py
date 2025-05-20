class InterfazNotificacionMail:
    
    def enviar_mail(self, destinatario, asunto, cuerpo):
        print(f"Enviando mail a {destinatario} con asunto '{asunto}' y cuerpo: {cuerpo}")
