import os
import numpy as np
from listaEncadenada import listaEncadenada

class DigrafoEncadenado:
    __arreglo: np.ndarray
    __cantidadV: int

    def __init__(self, cantidadV):
        self.__cantidadV = cantidadV
        self.__arreglo = np.empty(cantidadV, dtype=listaEncadenada)

        # Inicializar cada lista
        for i in range(cantidadV):
            self.__arreglo[i] = listaEncadenada()
    
    def crearArista(self, i, j):
        if (i <= self.__cantidadV and j <= self.__cantidadV) and (i >= 0 and j >= 0):
            self.__arreglo[i].insertar(j)
        else:
            print("Error: vertices no validos")

    def obtenerAdyacentes(self, vertice):
        lista = None
        
        if vertice >= 0 and vertice < self.__cantidadV:
            lista = self.__arreglo[vertice]
        else:
            print("Error: vertice no valido")
        
        return lista
    
    def esConexo(self):
        visitados = self.rep(self.NodoFuente())
        if len(visitados) == self.__cantidadV:
            return True
        else:
            return False
        
    def esAciclico(self):
        for i in range(self.__cantidadV):
            if self.esAciclicoRec(i, visitados=[False] * self.__cantidadV, padre=-1):
                return False
        return True
    
    def esAciclicoRec(self, vertice, visitados, padre):
        visitados[vertice] = True
        
        v = self.__arreglo[vertice].getCabeza()
        while v is not None:
            if not visitados[v.getDato()]:
                if self.esAciclicoRec(v.getDato(), visitados, vertice):
                    return True
            elif padre != v.getDato():
                return True
        return False
    
    def rea(self, verticeInicial): #Recorrido en anchura
        lista = []
        visitados = [False] * self.__cantidadV
        cola = [verticeInicial]

        while cola:
            vertice = cola.pop(0)
            lista.append(vertice)
            visitados[vertice] = True
            
            v = self.__arreglo[vertice].getCabeza()
            while v is not None:
                if not visitados[v.getDato()]:
                    cola.append(v.getDato())
                    visitados[v.getDato()] = True
                v = v.getSiguiente()
        
        return lista
    
    def rep(self, verticeInicial): #Recorrido en profundidad
        lista = []
        self.repRec(verticeInicial, [False] * self.__cantidadV, lista)
        return lista
        
    def repRec(self, vertice, visitados, lista):
        visitados[vertice] = True
        lista.append(vertice)
        
        cabeza = self.__arreglo[vertice].getCabeza()
        while cabeza is not None:
            if not visitados[cabeza.getDato()]:
                self.repRec(cabeza.getDato(), visitados, lista)
            cabeza = cabeza.getSiguiente()
 
    def camino(self, verticeInicial, verticeFinal):
        return verticeFinal in self.rep(verticeInicial)
           
    #Adicionales Digrafo
    def gradoEntrada(self, vertice):
        grado = 0
        for i in range(self.__cantidadV):
            if self.__arreglo[i].buscar(vertice) != -1:
                grado += 1
        return grado
    
    def gradoSalida(self, vertice):
        return self.__arreglo[vertice].getCantidad()
    
    #Nodo fuente: evalua si vertice es nodo funete
    def nodoFuente(self, vertice):
        if self.gradoEntrada(vertice) == 0:
            return True
        return False
    
    #Nodo sumidero: evalua si vertice es nodo sumidero
    def nodoSumidero(self, vertice):
        if self.gradoSalida(vertice) == 0:
            return True
        return False
    
    #Otros metodos
    def mostrarDigrafo(self):
        for i in range(self.__cantidadV):
            print(f'{i} --> ', end='')

            lista_vecinos = self.__arreglo[i].getCabeza()  # Obtener la cabeza de la lista
            while lista_vecinos is not None:
                print(f'{lista_vecinos.getDato()} --> ', end='')
                lista_vecinos = lista_vecinos.getSiguiente()
            
            print("None")  # Marcar el final de los vecinos
    
if __name__ == '__main__':
    os.system('cls')
    digrafo = DigrafoEncadenado(4)

    digrafo.crearArista(0, 1)
    digrafo.crearArista(0, 2)
    digrafo.crearArista(1, 3)
    digrafo.crearArista(2, 3)
    digrafo.mostrarDigrafo()

    print("Recorrido en anchura: ", digrafo.rea(0))
    print("Recorrido en profundidad: ", digrafo.rep(0))
    print("Es conexo: ", digrafo.esConexo())
    print("Camino entre 0 y 3: ", digrafo.camino(0, 3))