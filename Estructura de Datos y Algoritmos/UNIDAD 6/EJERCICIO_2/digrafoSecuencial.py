import numpy as np

class Digrafo:
    __cantidadV: int
    __matriz = None

    def __init__(self, n):
        self.__CantidadV = n
        self.__matriz = np.zeros((n, n), dtype=int)


    def crearArista(self, i, j):
        if (i <= self.__CantidadV and j <= self.__CantidadV) and (i >= 0 and j >= 0):
            self.__matriz[i][j] = 1
        else:
            print("Error: vertices no validos")

    
    def obtenerAdyacentes(self, vertice):
        adyacentes = []
        for j in range(0,self.__CantidadV):
            if self.__matriz[vertice][j] == 1:
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

        visitados[verticeInicial] = True
        lista.append(verticeInicial)

        while len(lista) != 0:
            vertice = lista.pop(0)
            print(vertice)

            for i in self.obtenerAdyacentes(vertice):
                if not visitados[i]:
                    visitados[i] = True
                    lista.append(i)

    def rep(self, verticeInicial):
        visitados = [False] * self.__CantidadV
        lista = []

        visitados[verticeInicial] = True
        lista.append(verticeInicial)

        while len(lista) != 0:
            vertice = lista.pop()
            print(vertice)

            for i in self.obtenerAdyacentes(vertice):
                if not visitados[i]:
                    visitados[i] = True
                    lista.append(i)
    
    def camino(self, verticeInicial, verticeFinal):
        visitados = [False] * self.__CantidadV
        lista = []

        self.caminoRec(verticeInicial, verticeFinal, visitados, lista)
        return lista

    def caminoRec(self, verticeInicial, verticeFinal, visitados, lista):
        visitados[verticeInicial] = True
        lista.append(verticeInicial)

        if verticeInicial == verticeFinal:
            return True

        for i in self.obtenerAdyacentes(verticeInicial):
            if not visitados[i]:
                if self.caminoRec(i, verticeFinal, visitados, lista):
                    return True
        lista.pop()
        return False


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


    # Operaciones ADICIONALES de Digrafo

    



if __name__ == '__main__':
    digrafo = Digrafo(5)
    digrafo.crearArista(0, 1)
    digrafo.crearArista(2, 0)
    digrafo.crearArista(1, 2)

    digrafo.mostrarDigrafo()
    digrafo.esConexo()
    print("Es Aciclico: ", digrafo.esAciclico())
    print("Camino desde 0 hasta 2: ", digrafo.camino(0, 2))