import numpy as np

class Nodo:
    __dato: int
    __siguiente: int

    def __init__(self, dato, siguiente=None):
        self.__dato = dato
        self.__siguiente = siguiente #type: ignore
    
    def getDato(self):
        return self.__dato
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setDato(self, dato):
        self.__dato = dato
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

class listaCursor:
    __arreglo: Nodo
    __cantidad: int
    __cabeza: int
    __disponible: int
    __dimension: int
    
    def __init__(self, dimension):
        self.__arreglo = np.empty(dimension, dtype = Nodo) #type: ignore
        self.__cantidad = 0 
        self.__cabeza = -1 #cabeza para la parte que maneja los espacios con contenido
        self.__disponible = 0 #cabeza para la parte que maneja los espacios vacios o dispuestos a alamacaenar contenido
        self.__dimension = dimension

        for i in range(dimension - 1):
            self.__arreglo[i] = Nodo(None, i+1)
        
        self.__arreglo[dimension - 1] = Nodo(None, -1) #type: ignore

    def vacia(self):
        return self.__cantidad == 0 #preguntar si podemos utilizar self.__cabeza
    
    def lleno(self):
        return self.__cantidad == self.__dimension #preguntar si podemos utilizar self.__disponible
    
    def buscar(self, dato):
        indice_actual = self.__cabeza
        while indice_actual != -1 and self.__arreglo[indice_actual].getDato() != dato:
            indice_actual = self.__arreglo[indice_actual].getSiguiente()
        return indice_actual

    def anterior(self, dato):
        pos = self.buscar(dato)
        if pos == -1:
            raise Exception("Dato no encontrado")
        else:
            indice_actual = self.__cabeza
            indice_anterior = -1
            while indice_actual != pos:
                indice_anterior = indice_actual
                indice_actual = self.__arreglo[indice_actual].getSiguiente()
            return self.__arreglo[indice_anterior].getDato()
        
    def siguiente(self, dato):
        pos = self.buscar(dato)
        if pos == -1:
            raise Exception("Dato no encontrado")
        else:
            siguiente = self.__arreglo[pos].getSiguiente()
            return self.__arreglo[siguiente].getDato()
    
    def insertar(self, dato):
        if self.vacia():
            self.__arreglo[self.__disponible].setDato(dato)
            self.__cabeza = self.__disponible
            self.__disponible = self.__arreglo[self.__disponible].getSiguiente()
            self.__arreglo[self.__cabeza].setSiguiente(-1)
            self.__cantidad += 1

        else:
            if self.lleno():
                raise Exception("Cursor lleno")  # Lista llena, no se puede insertar más elementos

            indice_actual = self.__cabeza
            indice_anterior = -1 
            
            #se busca la posicion segun el dato, y se busca el indice del anterior para que despues apunte al nuevo valor a insertar
            while indice_actual != -1 and self.__arreglo[indice_actual].getDato() < dato:
                indice_anterior = indice_actual
                indice_actual = self.__arreglo[indice_actual].getSiguiente()

            indice_nuevo = self.__disponible
            self.__disponible = self.__arreglo[self.__disponible].getSiguiente()
            
            if indice_anterior == -1:
                self.__arreglo[indice_nuevo].setSiguiente(self.__cabeza)
                self.__cabeza = indice_nuevo
            else:
                self.__arreglo[indice_nuevo].setSiguiente(indice_actual)
                self.__arreglo[indice_anterior].setSiguiente(indice_nuevo)
            
            self.__arreglo[indice_nuevo].setDato(dato)
            self.__cantidad += 1


    def eliminar(self, dato):
        if self.vacia():
            raise Exception("Cursor vacio")
        else:
            indice_actual = self.__cabeza
            indice_anterior = -1
            while indice_actual != -1 and self.__arreglo[indice_actual].getDato() != dato:
                indice_anterior = indice_actual
                indice_actual = self.__arreglo[indice_actual].getSiguiente()
            
            if indice_actual == -1:
                raise Exception("Dato no encontrado")
            else:
                if indice_anterior == -1:
                    self.__cabeza = self.__arreglo[self.__cabeza].getSiguiente()
                else:
                    self.__arreglo[indice_anterior].setSiguiente(self.__arreglo[indice_actual].getSiguiente())
                self.__arreglo[indice_actual].setDato(None)
                self.__arreglo[indice_actual].setSiguiente(self.__disponible)
                self.__disponible = indice_actual
                self.__cantidad -= 1
    
    def recorrer(self):
        indice_actual = self.__cabeza
        while indice_actual != -1:
            print(self.__arreglo[indice_actual].getDato())
            indice_actual = self.__arreglo[indice_actual].getSiguiente()

    
    #---Otros metodos visuales---#
    def recorrerArreglo(self):
        for i in range(self.__dimension - 1):
            print("Componente[{}]  Dato: {}   Puntero: {}".format(i,self.__arreglo[i].getDato(),self.__arreglo[i].getSiguiente() ))

if __name__ == '__main__':
    lista = listaCursor(7)
    lista.insertar(1)
    lista.insertar(4)
    lista.insertar(5)
    lista.insertar(2)
    lista.insertar(3)
    lista.recorrerArreglo()

    print("\n\n--------------------------------------------------------------------------")
    print("La posicion del elemento numero 4 es: ", lista.buscar(4))
    print("Anterior: ", lista.anterior(4))
    print("Siguiente: ", lista.siguiente(4))
    print("--------------------------------------------------------------------------")

    print("Eliminar el elemento 4")
    lista.eliminar(4)
    lista.recorrer()
    lista.recorrerArreglo()
    print("--------------------------------------------------------------------------")

    lista.insertar(4)
    lista.recorrer()
    lista.recorrerArreglo()

    
