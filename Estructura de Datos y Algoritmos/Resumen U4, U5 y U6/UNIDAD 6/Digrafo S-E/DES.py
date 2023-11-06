import numpy as np
from listaEncadenada import listaEncadenada

class DigrafoEncadenado:
    __arreglo: np.ndarray
    __cantidadV: int

    def __init__(self, cantidadV):
        self.__cantidadV = cantidadV
        self.__arreglo = np.empty(cantidadV, dtype=listaEncadenada)

        for i in range(cantidadV):
            self.__arreglo[i] = listaEncadenada()
    
    def crearArista(self, i, j):
        if (i <= self.__cantidadV and j <= self.__cantidadV) and (i >= 0 and j >= 0):
            self.__arreglo[i].insertar(j)
        else:
            print("Error: vertices no validos")

    def obtenerAdyacentes(self, vertice):
        lista = []
        aux = self.__arreglo[vertice].getCabeza()

        while aux is not None:
            lista.append(aux.getDato())
            aux = aux.getSiguiente()
        
        return lista
    
    def esAciclico(self):
        for i in range(self.__cantidadV):
            if self.esAciclicoRec(i, [False] * self.__cantidadV, -1):
                return False
        return True
    
    def esAciclicoRec(self, vertice, visitados, padre):
        visitados[vertice] = True
        
        for i in self.obtenerAdyacentes(vertice):
            if self.obtenerAdyacentes(i) != []:
                if not visitados[i]:
                    if self.esAciclicoRec(i, visitados, vertice):
                        return True
                elif i != padre:
                    return True
        
        return False
    
    def rea(self, verticeInicial): 
        lista = []
        visitados = [False] * self.__cantidadV
        cola = [verticeInicial]
        visitados[verticeInicial] = True

        while cola:
            vertice = cola.pop(0)
            lista.append(vertice)
            visitados[vertice] = True
            
            for i in self.obtenerAdyacentes(vertice):
                if not visitados[i]:
                    cola.append(i)
                    visitados[i] = True
                
        return lista
    
    def rep(self, verticeInicial):
        lista = []
        self.repRec(verticeInicial, [False] * self.__cantidadV, lista)
        return lista
        
    def repRec(self, vertice, visitados, lista):
        visitados[vertice] = True
        lista.append(vertice)
        
        for i in self.obtenerAdyacentes(vertice):
            if not visitados[i]:
                self.repRec(i, visitados, lista)

    def esConexo(self):
        return len(self.rep(self.NodoFuente())) == self.__CantidadV #type: ignore
 
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
        return len(self.obtenerAdyacentes(vertice))
    
    def nodoFuente(self, vertice):
        if self.gradoEntrada(vertice) == 0 and self.gradoSalida(vertice) > 0:
            return True
        return False
    
    def nodoSumidero(self, vertice):
        if self.gradoEntrada(vertice) > 0 and self.gradoSalida(vertice) == 0:
            return True
        return False
    
#-------------------------------------------------------------------------------------------------------------------------------------

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
    
    def esConexo(self):
        return len(self.rep(self.NodoFuente())) == self.__CantidadV
    
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
    
    def rea(self, verticeInicial): 
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
    
    def rep(self, verticeInicial):
        lista = []
        self.repRec(verticeInicial, [False] * self.__CantidadV, lista)
        return lista
    
    def repRec(self, verticeInicial, visitados, lista):
        visitados[verticeInicial] = True
        lista.append(verticeInicial)

        for i in self.obtenerAdyacentes(verticeInicial):
            if not visitados[i]:
                self.repRec(i, visitados, lista)

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
        return len(self.obtenerAdyacentes(vertice))
       
    def NodoFuente(self):
        for i in range(self.__CantidadV):
            if self.gradoDeEntrada(i) == 0 and self.gradoDeSalida(i) > 0:
                return i
        return -1
    
    def NodoSumidero(self):
        for i in range(self.__CantidadV):
            if self.gradoDeEntrada(i) > 0 and self.gradoDeSalida(i) == 0:
                return i
        return -1