import numpy as np
import os

class DigrafoSecuencial:
    __cantidadV: int
    __matriz = None

    def __init__(self, n):
        self.__CantidadV = n
        self.__matriz = np.zeros((n, n), dtype=int)

    def crearArista(self, i, j):
        if (i <= self.__CantidadV and j <= self.__CantidadV) and (i >= 0 and j >= 0):
            self.__matriz[i][j] = 1 #type: ignore
        else:
            print("Error: vertices no validos")

    def obtenerAdyacentes(self, vertice):
        adyacentes = []
        for j in range(0,self.__CantidadV):
            if self.__matriz[vertice][j] == 1: #type: ignore
                adyacentes.append(j)
        return adyacentes
    
    def esConexo(self): #Si todos los vertices estan conectados digrafo
        visitados = self.rep(self.NodoFuente())
        if len(visitados) == self.__CantidadV:
            return True
        else:
            return False
    
    def esAciclico(self):
        for i in range(self.__CantidadV):
            if self.esAciclicoRec(i, visitados=[False] * self.__CantidadV, padre=-1):
                return False
        return True
    
    def esAciclicoRec(self, vertice, visitados, padre):
        visitados[vertice] = True

        for i in self.obtenerAdyacentes(vertice) :
            if self.obtenerAdyacentes(i) != []:
                if not visitados[i]:
                    if self.esAciclicoRec(i, visitados, vertice):
                        return True
                elif i != padre:
                    return True
            else:
                return False
            
        return False
    
    def rea(self, verticeInicial): #Recorrido en anchura
        visitados = [False] * self.__CantidadV
        lista = []

        cola = [verticeInicial]
        visitados[verticeInicial] = True

        while cola:
            vertice = cola.pop(0)
            lista.append(vertice)

            for i in self.obtenerAdyacentes(vertice):
                if not visitados[i]:
                    cola.append(i)
                    visitados[i] = True

        return lista
    
    def rep(self, verticeInicial): #Recorrido en profundidad
        lista = []
        self.repRecursivo(verticeInicial, [False] * self.__CantidadV, lista)
        return lista
    
    def repRecursivo(self, verticeInicial, visitados, lista):
        visitados[verticeInicial] = True
        lista.append(verticeInicial)

        for i in self.obtenerAdyacentes(verticeInicial):
            if not visitados[i]:
                self.repRecursivo(i, visitados, lista)

    def camino(self, verticeInicial, verticeFinal):
        return verticeFinal in self.rep(verticeInicial)

    # Operaciones ADICIONALES de Digrafo
    def gradoDeEntrada(self, vertice):
        grado = 0
        for i in range(self.__CantidadV):
            if self.__matriz[i][vertice] == 1: #type: ignore
                grado += 1
        return grado

    def gradoDeSalida(self, vertice):
        grado = 0
        for j in range(self.__CantidadV):
            if self.__matriz[vertice][j] == 1: #type: ignore
                grado += 1
        return grado
    # Nodo Fuente: nodo que tiene grado de entrada 0
    def NodoFuente(self):
        for i in range(self.__CantidadV):
            if self.gradoDeEntrada(i) == 0:
                return i
        return -1
    # Nodo Sumidero: nodo que tiene grado de salida 0
    def NodoSumidero(self):
        for i in range(self.__CantidadV):
            if self.gradoDeSalida(i) == 0:
                return i
        return -1
    
    # Operaciones Extra    
    def mostrarDigrafo(self):
        print("Grafo: ")

        print("   ",end='')
        for k in range(self.__CantidadV):
            print("[{}]".format(k),end='')

        print()        
        for i in range(self.__CantidadV):
            print("[{}]".format(i),end='')
            for j in range(self.__CantidadV):
                print(" {} ".format(self.__matriz[i][j]),end='') #type: ignore 
            print()


if __name__ == '__main__':
    os.system('cls')
    digrafo = DigrafoSecuencial(4)

    digrafo.crearArista(0, 1)
    digrafo.crearArista(0, 2)
    digrafo.crearArista(1, 3)
    digrafo.crearArista(2, 3)
    digrafo.mostrarDigrafo()

    print("Recorrido en anchura: ", digrafo.rea(0))
    print("Recorrido en profundidad: ", digrafo.rep(0))
    print("Es conexo: ", digrafo.esConexo())
    print("Camino entre 0 y 3: ", digrafo.camino(0, 3))