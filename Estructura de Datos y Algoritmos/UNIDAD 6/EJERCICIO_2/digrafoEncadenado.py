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
    
    def agregarArista(self, i, j):
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
        i=0
        band= True

        while i < self.__cantidadV and band == True:
            if self.__arreglo[i].vacio() or self.__arreglo[i].getCantidad() != self.__cantidadV:
                band = False
            i+=1
        return band

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
        visitados = [False] * self.__cantidadV
        cola = []
        visitados[verticeInicial] = True
        cola.append(verticeInicial)
        while len(cola) != 0:
            vertice = cola.pop(0)
            print(vertice)
            for i in self.obtenerAdyacentes(vertice):
                if not visitados[i]:
                    visitados[i] = True
                    cola.append(i)

    def rep(self, verticeInicial): #Recorrido en profundidad
        visitados = [False] * self.__cantidadV
        visitados[verticeInicial] = True
        print(verticeInicial)
        for i in self.obtenerAdyacentes(verticeInicial):
            if not visitados[i]:
                self.repRec(i, visitados)

    def repRec(self, vertice, visitados):
        visitados[vertice] = True
        print(vertice)
        for i in self.obtenerAdyacentes(vertice):
            if not visitados[i]:
                self.repRec(i, visitados)
    
    def camino(self, verticeInicial, verticeFinal):
        visitados = [False] * self.__cantidadV
        visitados[verticeInicial] = True
        cola = []
        cola.append(verticeInicial)
        while len(cola) != 0:
            vertice = cola.pop(0)
            for i in self.obtenerAdyacentes(vertice):
                if i == verticeFinal:
                    return True
                if not visitados[i]:
                    visitados[i] = True
                    cola.append(i)
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
    os.system('clear')
    print("Digrafo Encadenado")
    digrafo = DigrafoEncadenado(5)
    digrafo.agregarArista(0, 1)
    digrafo.agregarArista(1, 1)
    digrafo.agregarArista(3, 1)
    digrafo.mostrar()
    print("Es conexo: ", digrafo.esConexo())
    print("Es aciclico: ", digrafo.esAciclico())
    digrafo.rea(2)
    digrafo.rep(2)
    print(digrafo.camino(2, 4))
    print(digrafo.camino(4, 2))