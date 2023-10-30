import numpy as np
import os 

class GrafoSecuencial:
    __CantidadV = 0
    __matriz = None

    def __init__(self, n):
        self.__CantidadV = n
        self.__matriz = np.zeros((n, n), dtype=int)

    def crearArista(self, i, j):
        if (i <= self.__CantidadV and j <= self.__CantidadV) and (i >= 0 and j >= 0):
            self.__matriz[i][j] = 1 #type: ignore
            self.__matriz[j][i] = 1 #type: ignore
        else:
            print("Error: vertices no validos")

    def obtenerAdyacentes(self, i):
        adyacentes = []
        for j in range(0,self.__CantidadV):
            if self.__matriz[i][j] == 1: #type: ignore
                adyacentes.append(j)
        return adyacentes

    def esConexo(self):
        band = True
        i = 0
        while band and i < self.__CantidadV:
            if len(self.obtenerAdyacentes(i)) == 0:
                band = False
            else:
                i+=1
        if band:
            print("El grafo es conexo")
        else:
            print("El grafo no es conexo")

    #Funciones para saber si es aciclico
    def esAciclico(self):
        i = 0
        band = True #Se inicializa la bandera en False
        while i < self.__CantidadV and band == True: #Se recorre el grafo
            if self.__matriz[i][i] == 1: #type: ignore
                print("el vertice {} tiene ciclo".format(i)) #Si se encuentra un ciclo, se imprime el vertice
                band = False #Si se encuentra un ciclo, se cambia la bandera a True
            i += 1
        return band #Se devuelve la bandera 
    
    def rea(self, verticeInicial): #Recorrido en anchura
        visitados = [False] * self.__CantidadV
        lista = []
        visitados[verticeInicial] = True
        lista.append(verticeInicial)
        while len(lista) > 0:
            vertice = lista.pop(0)
            print(vertice, end=' ')
            for i in self.obtenerAdyacentes(vertice):
                if not visitados[i]:
                    visitados[i] = True
                    lista.append(i)
        print()

    def rep(self, verticeInicial):
        visitados = [False] * self.__CantidadV
        self.repRecursivo(verticeInicial, visitados)
        print()

    def repRecursivo(self, vertice, visitados):
        visitados[vertice] = True
        print(vertice, end=' ')
        for i in self.obtener_adyacentes(vertice):
            if not visitados[i]:
                self.recorrido_en_profundidad_aux(i, visitados)
    
    def camino(self, origen, destino):
        visitados = [False] * self.__CantidadV #Lista de visitados: False = no visitado, True = visitado
        return self.caminoAux2(origen, destino, visitados, camino=[]) #Se llama a la funcion auxiliar y se devuelve el camino
    
    #En este primer camino se devuelve un booleano
    def caminoAux(self, origen, destino, visitados):
        visitados[origen] = True
        if origen == destino:
            return True
        for i in self.obtener_adyacentes(origen):
            if not visitados[i]:
                if self.caminoAux(i, destino, visitados):
                    return True
        return False

    #En este segundo camino se inserta en una lista el camino que se va recorriendo
    def caminoAux2(self, origen, destino, visitados, camino):
        visitados[origen] = True #Se marca como visitado
        camino.append(origen) #Se agrega a la lista camino
        
        if origen == destino: #Si el origen es igual al destino, se devuelve el camino
            return camino #Se devuelve el camino
        
        for i in self.obtenerAdyacentes(origen): #Se recorren los adyacentes del origen
            if not visitados[i]: #Si no esta visitado
                if self.caminoAux2(i, destino, visitados, camino): #Se llama recursivamente
                    return camino #Se devuelve el camino
        camino.pop() #Si no se encuentra el camino, se elimina el ultimo elemento de la lista

    def mostrarGrafo(self):
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
    os.system("cls")

    grafo = GrafoSecuencial(5)
    grafo.crearArista(1, 4)
    grafo.crearArista(1, 2)
    grafo.crearArista(1, 1)
    grafo.crearArista(2, 3)
    grafo.crearArista(2, 4)

    grafo.mostrarGrafo()
    print("Es Aciclico: ", grafo.esAciclico())
    #un grafo es aciclico si no tiene ciclos


    #print("Camino entre 1 y 3: ", grafo.camino(1, 3))
    print("\n\n")