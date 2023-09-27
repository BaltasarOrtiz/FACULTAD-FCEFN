class Nodo:
    __letra: None | str
    __frecuencia: None | int
    __siguiente: None
    __izquierdo: None
    __derecho: None
    
    def __init__(self, letra, frecuencia):
        self.__letra = letra
        self.__frecuencia = frecuencia
        self.__siguiente = None
        self.__izquierdo = None
        self.__derecho = None
         
    def getLetra(self):
        return self.__letra
    
    def getFrecuencia(self):
        return self.__frecuencia

    def getSiguiente(self):
        return self.__siguiente
    
    def getIzquierdo(self):
        return self.__izquierdo

    def getDerecho(self):
        return self.__derecho

    def setLetra(self, letra):
        self.__letra = letra
    
    def setFrecuencia(self, frecuencia):
        self.__frecuencia = frecuencia
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    
    def setIzquierdo(self, izquierdo):
        self.__izquierdo = izquierdo

    def setDerecho(self, derecho):
        self.__derecho = derecho