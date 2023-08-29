class Paciente:
    __nombre : str
    __dni : str
    __especialidad : int
    __tiempoLlegada : int

    def __init__(self, nombre, dni, especialidad, tiempoLlegada):
        self.__nombre = nombre
        self.__dni = dni
        self.__especialidad = especialidad
        self.__tiempoLlegada = tiempoLlegada

    def getEspecialidad(self):
        return self.__especialidad
    
    def getTiempoLlegada(self):
        return self.__tiempoLlegada

class Nodo:
    __dato : int|Paciente
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
    
class colaEncadenada:
    __primero : None|Nodo
    __ultimo : None|Nodo
    __cantidad : int

    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cantidad = 0

    def vacia(self):
        return self.__cantidad == 0
    
    def insertar(self, dato):
        nuevoNodo = Nodo(dato)
        if self.__ultimo == None:
            self.__primero = nuevoNodo
        else:
            self.__ultimo.setSiguiente(nuevoNodo)
        
        self.__ultimo = nuevoNodo
        self.__cantidad += 1
    
    def suprimir(self):
        if self.vacia():
            print("La cola esta vacia")
        else:
            x = self.__primero.getDato() #type: ignore
            self.__primero = self.__primero.getSiguiente() #type: ignore
            self.__cantidad -= 1

            if self.__primero is None: #esto lo utilizamos en el caso hipotetico de que nos quedemos sin elementos en el caso hipotetico
                self.__ultimo = None

            return x
    
    def recorrer(self):
        aux = self.__primero
        while aux != None:
            print("Elemento: ", aux.getDato())
            aux = aux.getSiguiente()
    
    def getCantidad(self):
        return self.__cantidad