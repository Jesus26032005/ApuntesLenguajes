class Evento: 
    def __init__(self, horaInicio, horaFinal, nombreContratista, telefono, colorMantel, pagoFinal=None, saldoPagado=None, saldoPendiente=None, dia=None , id=None):
        self._id = id
        self._horaInicio = horaInicio
        self._horaFinal = horaFinal
        self._nombreContratista = nombreContratista
        self._telefono = telefono
        self._colorMantel = colorMantel
        self._pagoFinal = pagoFinal
        self._saldoPagado =saldoPagado
        self._saldoPendiente = saldoPendiente
        self._dia = dia

    def __str__(self):
        return (f"Evento( id: {
            self._id
        },{self._horaInicio}, {self._horaFinal}, {self._nombreContratista}, "
                f"{self._telefono}, {self._colorMantel}, {self._pagoFinal}, "
                f"{self._saldoPagado}, {self._saldoPendiente}, {self._dia})")

    def actualizar_pago(self, cantidad):
        self._saldoPagado += cantidad
        self._saldoPendiente = self._pagoFinal - self._saldoPagado

    def es_pagado_completo(self):
        return self._saldoPendiente <= 0
    
    @property
    def horaInicio(self):
        return self._horaInicio
    @property
    def horaFinal(self):
        return self._horaFinal
    @property
    def nombreContratista(self):
        return self._nombreContratista
    @property
    def telefono(self):
        return self._telefono
    @property
    def colorMantel(self):
        return self._colorMantel
    @property
    def pagoFinal(self):
        return self._pagoFinal
    @property
    def saldoPagado(self):
        return self._saldoPagado
    @property
    def saldoPendiente(self):
        return self._saldoPendiente
    @property
    def dia(self):
        return self._dia
    @property
    def id(self):
        return self._id

    @horaFinal.setter
    def horaFinal(self, valor):
        self._horaFinal = valor
    @horaInicio.setter
    def horaInicio(self, valor):
        self._horaInicio = valor
    @nombreContratista.setter
    def nombreContratista(self, valor):
        self._nombreContratista = valor
    @telefono.setter
    def telefono(self, valor):
        self._telefono = valor
    @colorMantel.setter
    def colorMantel(self, valor):
        self._colorMantel = valor
    @pagoFinal.setter
    def pagoFinal(self, valor):
        self._pagoFinal = valor
    @saldoPagado.setter
    def saldoPagado(self, valor):
        self._saldoPagado = valor
    @saldoPendiente.setter
    def saldoPendiente(self, valor):
        self._saldoPendiente = valor
    @dia.setter
    def dia(self, valor):
        self._dia = valor

    @id.setter
    def id(self, valor):
        self._id = valor