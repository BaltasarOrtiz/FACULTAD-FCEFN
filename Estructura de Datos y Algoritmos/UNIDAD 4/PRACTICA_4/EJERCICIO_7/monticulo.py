import numpy as np
import os

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
    
    def esHoja(self, posicion):
        return posicion > self.__cantidad #Si la posición es mayor que la cantidad de elementos, es hoja

    #Operaciones del TAD
    def insertar(self, dato):  
        if self.lleno():
            print("Montículo lleno")
        else:
            #Inserto el dato en la última posición
            self.__cantidad += 1
            self.__arreglo[self.__cantidad] = dato
            pos = self.__cantidad

            #Se reordena el montículo
            padre= self.Padre(pos) #Obtengo el padre

            #Mientras el padre sea mayor que el hijo
            while self.__arreglo[pos] < self.__arreglo[padre]: 
                self.intercambiar(pos, padre) #Intercambio el padre con el hijo

                #Actualizo las posiciones
                pos = padre
                padre = self.Padre(pos)
    
    def eliminar_minimo(self, padre):
        hijoIzq = self.hijoIzquierdo(padre)
        hijoDer = self.hijoDerecho(padre)

        #Mientras no sea hoja y el padre sea mayor que alguno de sus hijos
        while not self.esHoja(hijoDer) and (self.__arreglo[padre] > self.__arreglo[hijoIzq] or self.__arreglo[padre] > self.__arreglo[hijoDer]):
            #Si el hijo izquierdo es menor que el hijo derecho
            if self.__arreglo[hijoIzq] < self.__arreglo[hijoDer]:
                self.intercambiar(padre, hijoIzq)
                padre = hijoIzq
            #Si el hijo derecho es menor que el hijo izquierdo
            else:
                self.intercambiar(padre, hijoDer)
                padre = hijoDer
            #Actualizo los hijos
            hijoIzq = self.hijoIzquierdo(padre)
            hijoDer = self.hijoDerecho(padre)

    def eliminar(self): 
        if self.vacio():
            print("Montículo vacío")
        else:
            eliminado = self.__arreglo[1] #Guardo el dato a eliminar

            self.__arreglo[1] = self.__arreglo[self.__cantidad] #Pongo el último elemento en la raíz 
            self.__arreglo[self.__cantidad] = 0 #seteo el último elemento en None
            self.__cantidad -= 1 #Decremento la cantidad de elementos

            self.eliminar_minimo(1) #Reordeno el montículo
            return eliminado
    
    #Otras operaciones: Mostrar montículo     
    def mostrarMonticulo(self, sangria=4):
            if self.__cantidad == 0:
                print("El montículo está vacío")
                return

            def mostrarMonticuloRec(posicion, cadena):
                print(str(self.__arreglo[posicion]))
                #Para el hijo derecho
                hijoDer = self.hijoDerecho(posicion)
                if hijoDer <= self.__cantidad:
                    if self.hijoIzquierdo(posicion) <= self.__cantidad:
                        print(cadena+ "├" + "─" * sangria, end="") 
                    else:
                        print(cadena+ "└" + "─" * sangria, end="")
                    mostrarMonticuloRec(hijoDer, cadena + "│" + " " *sangria)
                #Para el hijo izquierdo
                hijoIzq = self.hijoIzquierdo(posicion)
                if hijoIzq <= self.__cantidad:
                    print(cadena+ "└" + "─" * sangria, end="")
                    mostrarMonticuloRec(hijoIzq, cadena + " " *sangria)

            mostrarMonticuloRec(1, "")
        
if __name__ == '__main__':
    os.system("cls")
    m = Monticulo(10)
    m.insertar(1)
    m.insertar(2)
    m.insertar(3)
    m.insertar(4)
    m.insertar(5)
    m.insertar(6)
    m.insertar(7)

    print("Quirofano Lista de Espera:\n\n")
    print("#Contexto: Nivel de urgencia[1-10] siendo 1 el más urgente y 10 el menos urgente\n")
    m.mostrarMonticulo()

    bandera= True
    monticulo_desocupado = 5

    while bandera != False:
        if m.vacio():
            print("El Quirofano no tiene pacientes en espera")
            bandera = False
        else:
            if monticulo_desocupado == 0:
                print("El paciente de mayor urgencia se esta operando...")
                eliminado = m.eliminar()
                print("Quirofano saca de la lista al paciente con urgencia: ", eliminado)
                m.mostrarMonticulo()
                monticulo_desocupado = 5
            else:
                print("El Quirofano esta ocupado")
                monticulo_desocupado = 0
                print("hola")