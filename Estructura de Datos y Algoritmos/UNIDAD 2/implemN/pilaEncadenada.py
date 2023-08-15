class Nodo:
    __dato = None
    __sigNodo = None
    
    def __init__(self,dat):
        self.__dato = dat
        self.__sigNodo=None

    def  setItem(self,item):
        self.__dato=item
    
    def setSiguiente(self,siguiente):
        self.__sigNodo=siguiente

    def getSiguiente(self):
        return self.__sigNodo

    def getDato(self):
        return self.__dato


class PilaEncadenada:
    __top = None
    __cantidad: int
    def __init__(self):
        self.__top = None
        self.__cantidad = 0
    
    def insertar(self,dato):
        nuevaNodo = Nodo(dato)
        #nuevaNodo.setItem(input("Ingrese un dato: "))
        nuevaNodo.setSiguiente(self.__top)
        self.__top = nuevaNodo
        self.__cantidad+=1
        print("Elemento insertado correctamente ({})".format(nuevaNodo.getDato()))
    
    def Vacia(self):
        return self.__cantidad == 0

    def suprimir(self):
        if  not self.Vacia():
            aux=self.__top
            self.__top = self.__top.getSiguiente()
            self.__cantidad-=1
            print("Elemento {} eliminado correctamente".format(aux.getDato()))
            del aux
        else:
            print("La pila esta vacia")
    
    def mostrar(self):
        aux = self.__top
        if self.Vacia():
            print("La pila esta vacia")
        else:
            while aux != None:
                print("Dato: {}".format(aux.getDato()))
                aux = aux.getSiguiente()


if __name__ == "__main__":
    Pila = PilaEncadenada()
    Pila.insertar(1)
    Pila.insertar("Hola")
    Pila.insertar(True)
    Pila.insertar(3.1416)
    Pila.suprimir()
    Pila.mostrar()