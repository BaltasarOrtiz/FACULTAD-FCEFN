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
    
    def agregarArista(self, origen, destino):
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
        
        return lista

    def esConexo(self):
        i=0
        band= True

        while i < self.__cantidadV and band == True:
            if self.__arreglo[i].vacio() or self.__arreglo[i].getCantidad() != self.__cantidadV:
                band = False
            i+=1

        return band

    def esAciclico(self):
        i = 0
        band = False

        while i < self.__cantidadV and band == False:
            if self.__arreglo[i].vacio() or self.__arreglo[i].buscar(i) == -1:
                    band = True                  
            i += 1

        return band

    def rea (self, verticeInicial = 0): #Recorrido en anchura 
        visitados = [False] * self.__cantidadV
        self.reaRecursivo(verticeInicial, visitados)

    def reaRecursivo(self, verticeInicial, visitados):
        lista = []
        visitados[verticeInicial] = True
        lista.append(verticeInicial)

        while len(lista) > 0:
            vertice = lista.pop(0)
            print(vertice, end = " ")
            
            nodo = self.__arreglo[vertice].getCabeza()
            
            while nodo is not None:
                vecino = nodo.getDato()
                if not visitados[vecino]:
                    visitados[vecino] = True
                    lista.append(vecino)
                nodo = nodo.getSiguiente()
            
    def rep (self, verticeInicial = 0): #Recorrido en profundidad
        visitados = [False] * self.__cantidadV
        self.repRecursivo(verticeInicial, visitados)

    def repRecursivo(self, verticeInicial, visitados):
        visitados[verticeInicial] = True
        print(verticeInicial, end = " ")
        
        # Iterar a través de la lista encadenada del vértice
        nodo = self.__arreglo[verticeInicial].getCabeza()
        while nodo is not None:
            vecino = nodo.getDato()
            if not visitados[vecino]:
                self.repRecursivo(vecino, visitados)
            nodo = nodo.getSiguiente()
    
    def camino(self, origen, destino):
        lista = []  # Lista para almacenar el camino
        visitados = [False] * self.__cantidadV  # Lista para marcar los vértices visitados
        self.caminoRecursivo(origen, destino, visitados, lista)
        return lista

    def caminoRecursivo(self, actual, destino, visitados, lista):
        # Marcar el vértice actual como visitado y agregarlo a la lista
        visitados[actual] = True
        lista.append(actual)

        # Caso base: si se alcanza el destino, se encontró un camino
        if actual == destino:
            return True

        # Recorrer los vecinos del vértice actual
        nodo = self.__arreglo[actual].getCabeza()
        while nodo is not None:
            vecino = nodo.getDato()

            # Si el vecino no ha sido visitado, intentar encontrar un camino desde él
            if not visitados[vecino]:
                if self.caminoRecursivo(vecino, destino, visitados, lista):
                    return True

            nodo = nodo.getSiguiente()

        # Si no se encontró un camino desde este vértice, desmarcarlo y retroceder
        lista.pop()
        return False
        
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
    grafo = GrafoEncadenado(5)
    #Grafo conexo

    grafo.agregarArista(0,1)
    grafo.agregarArista(0,2)
    grafo.agregarArista(1,3)
    grafo.agregarArista(2,3)


    grafo.mostrar()
    
    print("\n\n")
    #print(f"Aciclico (significa que no tiene ciclos): {grafo.esAciclico()} <-- si es True, es aciclico")
    #print(f"Conexo (significa que todos los vertices estan conectados): {grafo.esConexo()} <-- si es True, es conexo")
    
    #print("Recorrido en anchura")
    #grafo.rea()
    #print("\n")
    #print("Recorrido en profundidad")
    #grafo.rep()

    print("Camino de 0 a 3: ",grafo.camino(0,3))
    print("Camino de 0 a 0: ",grafo.camino(0,0))
    print("Camino de 0 a 4: ",grafo.camino(0,4))



    """  
  0
 / \
1   2
/   
3
Recorrido en Anchura (BFS):Comenzando desde el vértice A, 
el recorrido BFS visitaría los vértices en el siguiente orden: 
0, 1, 2, 3. El recorrido BFS explora todos los 
vecinos de un vértice antes de pasar al siguiente nivel.

Recorrido en Profundidad (DFS):Comenzando desde el vértice A, 
el recorrido DFS visitaría los vértices en el siguiente orden: 
0, 1, 3, 2. El recorrido DFS explora profundamente un camino 
antes de retroceder y explorar otros caminos."""