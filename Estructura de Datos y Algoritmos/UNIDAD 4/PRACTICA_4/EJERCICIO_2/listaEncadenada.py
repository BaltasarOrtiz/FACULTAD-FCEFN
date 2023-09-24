from nodo import NodoLista
    
class listaEncadenada:
    __cabeza = None
    __cantidad: int
    
    def __init__ (self):
        self.__cabeza = None
        self.__cantidad = 0
    
    def vacio(self):
        return self.__cabeza == None

    def anterior(self, dato):
        pos = self.buscar(dato)
        if pos == -1 or pos == self.__cabeza:
            print('No existe el dato o es el primer elemento')
        else:
            return pos.getDato()
        
    def siguiente(self, dato):
        pos = self.buscar(dato)
        if pos == -1 or pos == self.__cantidad:
            print('No existe el dato o es el ultimo elemento')
        else:
            return pos.getSiguiente().getDato() #type: ignore
    
    def buscar(self, dato):
        aux = self.__cabeza
        
        while aux != None and aux.getDato() != dato:
            aux = aux.getSiguiente() #type: ignore
        
        if aux == None:
            return -1
        else:
            return aux

    def insertar(self, dato):
        nuevo = NodoLista(dato)
        if self.vacio() or dato < self.__cabeza.getDato(): #type: ignore
            nuevo.setSiguiente(self.__cabeza) #type: ignore
            self.__cabeza = nuevo
        else:
            aux = self.__cabeza
            anterior = None
            
            while aux is not None and dato > aux.getDato():
                anterior = aux
                aux = aux.getSiguiente() #type: ignore

            nuevo.setSiguiente(aux) #type: ignore
            anterior.setSiguiente(nuevo) #type: ignore
    
    def eliminar(self, dato):
        aux = self.__cabeza
        anterior = None

        while aux != None and aux.getDato() != dato:
            anterior = aux
            aux = aux.getSiguiente() #type: ignore
        
        if aux == None:
            print("El dato no existe")
        elif anterior == None:
            self.__cabeza = aux.getSiguiente() #type: ignore
        else:
            anterior.setSiguiente(aux.getSiguiente()) #type: ignore

    def mostrar(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente() #type: ignore
   