import numpy
import os

class ListaSecuencial:
    __arre = None
    __ultimo: int
    __cantidad: int

    def __init__(self, tam):
        self.__arre = numpy.empty(tam, dtype=int)
        self.__ultimo = -1
        self.__cantidad = tam
    
    def lleno(self):
        return self.__ultimo == self.__cantidad - 1
    
    def vacia(self):
        return self.__ultimo == -1

    def anterior(self, dato):
        pos = self.buscar(dato)
        if pos == -1 or pos == 0: #si no existe o el elemento a buscar es el primero
            print('No existe el dato o es el primer elemento')
        else:
            return self.__arre[pos - 1] #type: ignore
    
    def siguiente(self, dato):
        pos = self.buscar(dato)
        if pos == -1 or pos == self.__ultimo: #si no existe o el elemento a buscar es el ultimo entonces
            print('No existe el dato o es el ultimo elemento')
        else:
            return self.__arre[pos + 1] #type: ignore

    def primerElemento(self):
        if not self.vacia():
            print('Lista vacia')
        else:
            return self.__arre[0] #type: ignore
    
    def ultimoElemento(self):
        if not self.vacia():
            print('Lista vacia')
        else:
            return self.__arre[self.__ultimo] #type: ignore

    def insertar(self, dato):
        if self.lleno():
            print('Lista llena')

        elif self.__ultimo == -1:
            self.__ultimo += 1
            self.__arre[self.__ultimo] = dato #type: ignore
        else:
            pos = self.__ultimo
            while pos >= 0 and dato < self.__arre[pos]: #type: ignore
                pos -= 1

            #while encuentra la posicion en donde se debe insertar
            
            for i in range(self.__ultimo, pos, -1): #1 hasta 0 
                self.__arre[i + 1] = self.__arre[i] #type: ignore
            
            #for genera el shifteo para mover los datos 

            self.__arre[pos + 1] = dato #type: ignore
            self.__ultimo += 1
            
            #se inserta en la posicion 

    def buscar(self, dato): #busqueda binaria
        pos = -1
        izq = 0
        der = self.__ultimo
        while izq <= der and pos == -1:
            centro = (izq + der) // 2
            if dato == self.__arre[centro]: #type: ignore
                pos = centro
            elif dato < self.__arre[centro]: #type: ignore
                der = centro - 1
            else:
                izq = centro + 1
        return pos

    def eliminar(self, dato): 
        pos = self.buscar(dato)
        if pos != -1:
            i = pos
            for i in range(pos, self.__ultimo, -1):
                self.__arre[i] = self.__arre[i + 1] #type: ignore

            self.__ultimo -= 1
            print('El dato se elimino correctamente')
        else:
            print('El dato no se encuentra en la lista')

    def recorrer(self):
        for i in range(self.__ultimo + 1):
            print(self.__arre[i]) #type: ignore

if __name__ == '__main__':
    os.system("cls")
    listaSec = ListaSecuencial(5)
    listaSec.insertar(5)
    listaSec.insertar(3)
    listaSec.insertar(4)
    listaSec.insertar(1)
    listaSec.insertar(2)
    
    print("--------------------Mostrando elementos de la lista--------------------")
    listaSec.recorrer()
    print("-----------------------------------------------------------------------")
    print("\n")
    print("Elemento siguiente de {} es: {}".format(3, listaSec.siguiente(3)))
    print("Elemento anterior de {} es: {}".format(3, listaSec.anterior(3)))
    print("\n")
    
    """
    pos = listaSec.buscar(5)
    if pos != -1:
        print('El dato se encuentra en la posicion', pos)
    else:
        print('El dato no se encuentra en la lista')

    listaSec.eliminar(5)

    listaSec.recorrer()"""

