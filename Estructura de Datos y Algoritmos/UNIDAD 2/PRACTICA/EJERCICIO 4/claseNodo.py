class Nodo: 
    __dato = int
    __siguiente = None

    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def getDato(self):
        return self.__dato
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setDato(self, dato):
        self.__dato = dato

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente