class Clase:
    def __init__(self,nombre, profesor, mensualidad, pagoHecho, pagoRestante, horario= "Pendiente", id=None):
        self._nombreClase= nombre
        self._profesor= profesor
        self._horario= horario
        self._mensualidad = mensualidad
        self._pagoHecho= pagoHecho
        self._pagoRestante= pagoRestante

    def __str__(self):
        return f'La clase {self._nombreClase} es dada por el profesor {self._profesor} en el horario de {self._horario}, su mensualidad es de {self._mensualidad} y lo que lleva pagado es {self._pagoHecho} quedando a deber {self._pagoRestante}'

    def agregarPago(self, anadidoPago):
        self._pagoHecho+= anadidoPago

    def cambiarMensualidad(self, nuevaMensualidad):
        self._mensualidad= nuevaMensualidad


    @property
    def nombreClase(self):
        return self._nombreClase

    @property
    def profesor(self):
        return self._profesor

    @property
    def horario(self):
        return self._horario

    @property
    def mensualidad(self):
        return self._mensualidad

    @property
    def pagoHecho(self):
        return self._pagoHecho

    @property
    def pagoRestante(self):
        return self._pagoRestante

    @nombreClase.setter
    def nombreClase(self, valor):
        self._nombreClase = valor

    @profesor.setter
    def profesor(self, valor):
        self._profesor = valor

    @horario.setter
    def horario(self, valor):
        self._horario = valor

    @mensualidad.setter
    def mensualidad(self, valor):
        self._mensualidad = valor

    @pagoHecho.setter
    def pagoHecho(self, valor):
        self._pagoHecho = valor

    @pagoRestante.setter
    def pagoRestante(self, valor):
        self._pagoRestante = valor