class NodoArbol:
    __dato = None
    __izquierdo: None
    __derecho: None
    
    def __init__(self, dato):
        self.__dato = dato
        self.__izquierdo = None
        self.__derecho = None
        
    def getDato(self):
        return self.__dato
    
    def getIzquierdo(self):
        return self.__izquierdo

    def getDerecho(self):
        return self.__derecho
    
    def setDato(self, dato):
        self.__dato = dato
    
    def setIzquierdo(self, izquierdo):
        self.__izquierdo = izquierdo
        
    def setDerecho(self, derecho):
        self.__derecho = derecho
        

class NodoLista:
    __dato = None
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