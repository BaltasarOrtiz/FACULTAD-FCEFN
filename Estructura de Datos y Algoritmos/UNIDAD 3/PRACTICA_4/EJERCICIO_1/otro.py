from nodo import Nodo

class Arbol:
    __raiz: Nodo|None
    __cantidad: int

    def __init__(self):
        self.__raiz = None
        self.__cantidad = 0    

    def vacio(self):
        return self.__raiz == None
    
    def getRaiz(self):
        return self.__raiz

    def insertarRaiz(self,dato): #Caso 1
        nuevoNodo = Nodo(dato)
        self.__raiz = nuevoNodo
    
    def insertarOtro(self, nodo, dato): #Caso 2
        nuevoNodo = Nodo(dato)
        if dato < nodo.getDato():
            if nodo.getIzquierdo() == None:
                nodo.getIzquierdo(nuevoNodo)
            else:
                self.insertarOtro(nodo.getIzquierdo(), dato)
        elif dato > nodo.getDato():
            if nodo.getDerecho() == None:
                nodo.getDerecho(nuevoNodo)
            else:
                self.insertarOtro(nodo.getDerecho(), dato)
        else:
            print("El dato ya existe en el arbol")
    
    def insertar(self, dato): # insertar en el arbol
        if self.vacio():
            self.insertarRaiz(dato)
        else:
            self.insertarOtro(self.getRaiz(), dato)
    
    #-----------------------------------------------------------------------------------------
    # Otros metodos para ver el arbol mejor
    def mostrar(self, aux, espacio):
        if aux == 1:
            self.mostrar(aux = self.__raiz, espacio="")

        elif aux != None:
            self.mostrar(aux.getDerecho(),espacio+"   ")
            print(espacio,aux.getDato())
            self.mostrar(aux.getIzquierdo(),espacio+"   ")
    #-----------------------------------------------------------------------------------------