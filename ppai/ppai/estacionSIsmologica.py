class EstacionSismologica:
    def __init__(self, codigoEstacion, documentoCertificacionAdq, fechaSolicitudCreacion, latitud, longitud, nombre, nroCertificacionAdquisicion, sismografo=None):
        self.codigoEstacion = codigoEstacion
        self.documentoCertificacionAdq = documentoCertificacionAdq
        self.fechaSolicitudCreacion = fechaSolicitudCreacion
        self.latitud = latitud
        self.longitud = longitud
        self.nombre = nombre
        self.nroCertificacionAdquisicion = nroCertificacionAdquisicion
        self.sismografo = sismografo

    def getCodigoEstacion(self):
        return self.codigoEstacion

    def setCodigoEstacion(self, codigoEstacion):
        self.codigoEstacion = codigoEstacion

    def getDocumentoCertificacionAdq(self):
        return self.documentoCertificacionAdq

    def setDocumentoCertificacionAdq(self, documentoCertificacionAdq):
        self.documentoCertificacionAdq = documentoCertificacionAdq

    def getFechaSolicitudCreacion(self):
        return self.fechaSolicitudCreacion

    def setFechaSolicitudCreacion(self, fechaSolicitudCreacion):
        self.fechaSolicitudCreacion = fechaSolicitudCreacion

    def getLatitud(self):
        return self.latitud

    def setLatitud(self, latitud):
        self.latitud = latitud

    def getLongitud(self):
        return self.longitud

    def setLongitud(self, longitud):
        self.longitud = longitud

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNroCertificacionAdquisicion(self):
        return self.nroCertificacionAdquisicion

    def setNroCertificacionAdquisicion(self, nroCertificacionAdquisicion):
        self.nroCertificacionAdquisicion = nroCertificacionAdquisicion

    def getIdentificadorSismografo(self):
        if self.sismografo:
            return self.sismografo.getIdentificadorSismografo()
        return None

    def setSismografo(self, sismografo):
        self.sismografo = sismografo

    def cerrarServicio(self):
        if self.sismografo:
            self.sismografo.cerrarServicio()