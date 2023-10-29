import os
import numpy as np
from listaEncadenada import listaEncadenada

class GrafoEncadenado:
    __arreglo: np.ndarray
    __cantidadV: int

    def __init__(self, cantidadV: int):
        self.__cantidadV = cantidadV
        self.__arreglo = np.empty(cantidadV, dtype=listaEncadenada)

        # Inicializar cada lista
        for i in range(cantidadV):
            self.__arreglo[i] = listaEncadenada()
    
    def agregarArista(self, origen, destino): # Agregar arista: origen -> destino con peso donde peso es opcional
        self.__arreglo[origen].insertar(destino) # Insertar en la lista de origen
        self.__arreglo[destino].insertar(origen) # Insertar en la lista de destino
        
    def eliminarArista(self, origen, destino):
        self.__arreglo[origen].eliminar(destino)
        self.__arreglo[destino].eliminar(origen)
    
    def getAdyacentes(self, vertice):
        lista = None
        if vertice >= 0 and vertice < self.__cantidadV:
            lista = self.__arreglo[vertice]
        else:
            print("Error: vertice no valido")
        
        #lista.mostrar() #type: ignore
        return lista

    def esConexo(self):
        band = True
        i=0
        while i < self.__cantidadV and band != False:
            print(self.getAdyacentes(i).getCantidad()) #type: ignore
            if self.getAdyacentes(i).getCantidad() == 0: #type: ignore
                band = False
            i += 1
        
        if band == True:
            print("El grafo no es conexo")                
        else:
            print("El grafo es conexo")

    def mostrar(self):
        for i in range(self.__cantidadV):
            print(f'{i} --> ', end='')

            lista_vecinos = self.__arreglo[i].getCabeza()  # Obtener la cabeza de la lista
            while lista_vecinos is not None:
                print(f'{lista_vecinos.getDato()} --> ', end='')
                lista_vecinos = lista_vecinos.getSiguiente()
            
            print("None")  # Marcar el final de los vecinos

if __name__ == '__main__':
    os.system("cls")
    grafo = GrafoEncadenado(2)
    #Grafo conexo
    grafo.agregarArista(0, 1)
    grafo.agregarArista(1, 1)
    grafo.agregarArista(0, 0)
    grafo.agregarArista(1, 0)
    grafo.mostrar()
    print("\n\n")
    print("Conexo: ")
    grafo.esConexo()
    #grafo.getAdyacentes(0)
    