
#2 a la n-1
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

class PilaEncadenada:
    __tope = None
    __cant = int

    def __init__(self):
        self.__tope = None
        self.__cant = 0
    
    def Vacia(self):
        return self.__cant == 0

    def insertar(self, dato):
        nuevoNodo = Nodo(dato)
        nuevoNodo.setSiguiente(self.__tope)
        self.__tope = nuevoNodo
        self.__cant+=1
        print("Elemento insertado correctamente ({})".format(nuevoNodo.getDato()))


    def suprimir(self):
        if not self.Vacia():
            aux=self.__tope
            self.__tope = self.__tope.getSiguiente()
            self.__cant-=1
            print("Elemento {} eliminado correctamente".format(aux.getDato()))
        else:
            print("La pila esta vacia")

    def mostrar(self):
        aux = self.__tope
        if self.Vacia():
            print("La pila esta vacia")
        else:
            while aux != None:
                print("Dato: {}".format(aux.getDato()))
                aux = aux.getSiguiente()


if __name__ == '__main__':
    Pila = PilaEncadenada()
    Pila.insertar(1)
    Pila.insertar(2)
    Pila.insertar(3)
    Pila.insertar(4)
    #Pila.suprimir()
    print("Mostrando pila:")
    Pila.mostrar()