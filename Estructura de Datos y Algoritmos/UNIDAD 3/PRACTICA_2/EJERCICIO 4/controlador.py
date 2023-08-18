import os
from torre import Torre
from torre import Ficha


class Juego:
    __torres: list
    __cantDisc: int

    def __init__(self, ct):
        self.__torres = [Torre(ct) for _ in range(3)] #creo 3 torres
        self.__cantDisc =  ct

        for i in range(ct, 0, -1): #ct=valor inicial del rango, 0=valor final del rango, -1=paso o incremento negativo
            self.__torres[0].insertar(Ficha(i))
    
    def movimientoDisco(self, desde, hasta): #desde-1 hasta-1 porque el usuario ingresa 1,2,3 y yo necesito 0,1,2 por la disposicion secuencial
        if not self.__torres[desde].vacia(): #si la torre desde donde muevo el disco no esta vacia puedo realizar un movimiento
            ficha = self.__torres[desde].suprimir() #traigo la ficha desde la torre origen quitandola de la cabeza de la pila
            self.__torres[hasta].insertar(ficha)
        else:
            print("No quedan discos en la torre origen")

    def __str__(self):
        string = ""
        for i in range(ct,0,-1): #me permite visualizar mejor las fichas en la consola
            string+=("|{}|      |{}|      |{}|\n".format(self.__torres[0].obtenerFicha(i),self.__torres[1].obtenerFicha(i),self.__torres[2].obtenerFicha(i)))
        return string

    def termina(self):
        return self.__cantDisc == self.__torres[1].cantDiscos() and self.__cantDisc == self.__torres[2].cantDiscos()


if __name__ == '__main__':
    ct = 3
    TorreHanoi = Juego(ct)
    movimientos = 0 
    fin = False
    while not TorreHanoi.termina() and not fin:
        print(TorreHanoi)
        desde = int(input("Ingrese torre de origen: "))
        hasta = int(input("Ingrese torre de destino: "))

        os.system('cls')
        TorreHanoi.movimientoDisco(desde-1, hasta-1)
        movimientos+=1
        if input("Desea terminar el juego? S/N: ").lower() == "s":
            fin = True
        
    
    print("------Juego terminado------")
    print("Movimientos realizados: ", movimientos, "\n")
    print("Movimientos que se podrian haber realizado: ", 2**ct-1)#2^n-1
    print("Estado final de las torres...")
    print(TorreHanoi)