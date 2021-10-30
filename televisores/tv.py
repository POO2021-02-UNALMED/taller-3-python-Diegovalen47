class TV:

    _numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        self._control = None
        TV._numTV += 1

    def volumenUp(self):
        if self._volumen != 7 and self._estado:
            self._volumen += 1

    def volumenDown(self):
        if self._volumen != 0 and self._estado:
            self._volumen -= 1

    def canalUp(self):
        if self._canal != 120 and self._estado:
            self._canal += 1

    def canalDown(self):
        if self._canal != 1 and self._estado:
            self._canal -= 1

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    def getMarca(self):
        return self._marca;

    def getCanal(self):
        return self._canal;

    def getPrecio(self):
        return self._precio;

    def getVolumen(self):
        return self._volumen

    def getControl(self):
        return self._control

    def getEstado(self):
        return self._estado

    def setMarca(self, marca):
        self._marca = marca

    def setCanal(self, canal):
        if self._estado and canal >= 1 and canal <= 120:
            self._canal = canal

    def setPrecio(self, precio):
        self._precio = precio

    def setVolumen(self, volumen):
        self._volumen = volumen

    def setControl(self, control):
        self._control = control

    @classmethod
    def setNumTV(self, numTV):
        TV._numTV = numTV