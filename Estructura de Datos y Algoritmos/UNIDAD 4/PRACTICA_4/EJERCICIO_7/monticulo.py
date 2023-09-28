"""Ejercicio Nº7: Codifique un programa que simule 
el funcionamiento de la lista de espera del quirófano de un hospital. 
Cada vez que el quirófano esté desocupado, se operará al paciente de mayor urgencia, 
dentro de esa lista de espera. Al ingresar un paciente al hospital, 
además de solicitarle los datos personales, 
se le asignará una prioridad relacionada con la gravedad de su caso."""

#TAD Montículo Binario
#Implementación: Montículo Binario con arreglo/numpy

import numpy as np

class Monticulo:
    __arreglo : np.ndarray
    __cantidad : int
    __dimension : int

    def __init__(self, dimension):
        self.__arreglo = np.empty(dimension, dtype = int)
        self.__cantidad = 0
        self.__arreglo[0] = -1
        self.__dimension = dimension
    
    def vacio(self):
        return self.__cantidad == 0

    def lleno(self):
        return self.__cantidad == self.__dimension
    
    #Elementos del montículo
    def Padre(self, posicion):
        return posicion // 2
    
    def hijoIzquierdo(self, posicion):
        return posicion * 2

    def hijoDerecho(self, posicion):
        return (posicion * 2) + 1

    #Operaciones del montículo
    def intercambiar(self, pos1, pos2):
        aux = self.__arreglo[pos1]
        self.__arreglo[pos1] = self.__arreglo[pos2]
        self.__arreglo[pos2] = aux
    
    def insertar(self, dato):  #0:[-1]  1:[10]  2:[]  3:[]   4:[]   5:[]   lote: 10 20 30 40 50 60
        if self.lleno():
            print("Montículo lleno")
        else:
            self.__cantidad += 1
            self.__arreglo[self.__cantidad] = dato
            pos = self.__cantidad

            padre= self.Padre(pos)
            while self.__arreglo[pos] < self.__arreglo[padre]:
                self.intercambiar(pos, padre)
                pos = padre
                padre = self.Padre(pos)

    
    def mostrar(self):
        print("Montículo: ", end = "")
        for i in range(1, self.__cantidad + 1):
            print(self.__arreglo[i], end = " ")
        print()
    
    def mostrarArbol(self):
        print("\n\nArbol: ")
        for i in range(1, self.__cantidad + 1):
            print("Nodo: ", self.__arreglo[i], end = " ")
            if self.hijoIzquierdo(i) <= self.__cantidad:
                print("Hijo Izquierdo: ", self.__arreglo[self.hijoIzquierdo(i)], end = " ")
            if self.hijoDerecho(i) <= self.__cantidad:
                print("Hijo Derecho: ", self.__arreglo[self.hijoDerecho(i)], end = " ")
            print()
        print()
            
if __name__ == '__main__':
    m = Monticulo(10)
    m.insertar(10)
    m.insertar(20)
    m.insertar(30)
    m.insertar(40)
    m.insertar(50)
    m.insertar(60)
    m.insertar(70)
    m.mostrar()
    m.mostrarArbol()