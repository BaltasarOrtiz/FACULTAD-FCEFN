from claseNodo import Nodo

class Pila2:
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

