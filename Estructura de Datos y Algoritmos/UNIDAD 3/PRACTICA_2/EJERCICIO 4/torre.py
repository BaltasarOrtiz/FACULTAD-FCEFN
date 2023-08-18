import numpy as np

class Ficha:
    __valor = int

    def __init__(self,valor=0):
        self.__valor = valor
    
    def getValor(self):
        return self.__valor
    
    def __str__(self) -> str:
        return str(self.__valor)


class Torre:
    __items = None
    __tope: int

    def __init__(self, dimension):
        self.__items = np.empty(dimension, dtype=Ficha)
        self.__tope = 0

    def vacia(self):
        return self.__tope == 0
    
    def insertar(self, ficha):
        if self.vacia():
            self.__items[self.__tope] = ficha #type:ignore
        elif self.getUltimaFicha() >= ficha.getValor():
            self.__items[self.__tope] = ficha #type:ignore
        else:
            raise Exception("No se puede insertar el disco encima de uno mas chico")
        self.__tope+=1

    def getUltimaFicha(self):
        return self.__items[self.__tope-1].getValor() #type:ignore

    def suprimir(self):
        if not self.vacia():
            self.__tope -= 1
            d = self.__items[self.__tope] #type:ignore
            return d
        else:
            raise Exception("La torre esta vacia")

    def cantDiscos(self):
        return self.__tope
    
    def obtenerFicha(self,i): #me permite visualizar mejor las fichas en la consola
        if self.__tope < i:
            return " "
        else:
            return self.__items[i-1] #type: ignore
    
