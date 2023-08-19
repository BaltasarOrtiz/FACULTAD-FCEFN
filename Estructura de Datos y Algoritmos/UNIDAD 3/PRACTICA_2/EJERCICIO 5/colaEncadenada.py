
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

class ColaEncadenada:
    __cant: int
    __pr = None
    __ul = None

    def __init__(self):
        self.__cant = 0
        self.__pr = None
        self.__ul = None
    
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.vacia():
            self.__pr = nuevo
        else:
            self.__ul.setSiguiente(nuevo) #type: ignore
        self.__ul = nuevo
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            print("La cola esta vacia")
        else:
            x = self.__pr.getDato() #type: ignore
            self.__pr = self.__pr.getSiguiente() #type: ignore
            self.__cant -= 1
            return x
    
    def recorrer(self):
        aux = self.__pr
        while aux != None:
            print("Elemento: ", aux.getDato())
            aux = aux.getSiguiente()
    

if __name__ == '__main__':
    cola = ColaEncadenada()
    print("Insertando elementos")
    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)
    print("Mostrando Elementos")    
    cola.recorrer()
    print("\nSuprimiendo Elemento: ", cola.suprimir())
    print("Mostrando Elementos")    
    cola.recorrer()
