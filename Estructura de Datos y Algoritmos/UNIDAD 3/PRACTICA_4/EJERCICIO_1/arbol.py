from nodo import Nodo


class ArbolBinarioBusqueda:
    __raiz : Nodo|None
    __cantidad : int
   
    def __init__(self):
        self.__raiz = None #type: ignore
        self.__cantidad = 0
    
    def vacio(self):
        return self.__raiz == None
    
    def getRaiz(self):
        return self.__raiz
    
    def insertar(self, subArbol, dato):
        if subArbol == None: 
            self.__raiz = Nodo(dato)
        else:
            if dato < subArbol.getDato(): #validamos si el dato es menor
                if subArbol.getIzquierdo() == None: #validamos si el nodo izquierdo esta vacio
                    subArbol.setIzquierdo(Nodo(dato))
                else: #si no esta vacio, llamamos recursivamente a la funcion
                    self.insertar(subArbol.getIzquierdo(), dato)

            elif dato > subArbol.getDato(): #lo mismo pero con el mayor
                    if subArbol.getDerecho() == None:
                        subArbol.setDerecho(Nodo(dato))
                    else:
                        self.insertar(subArbol.getDerecho(), dato)
            else:
                    print("Dato ya ingresado")

        self.__cantidad += 1
    
    def suprimir(self, subArbol, dato):
        pass
            
    
    def mostrar(self, subArbol, espacio):
        if subArbol != None:
            self.mostrar(subArbol.getDerecho(),espacio+"   ")
            print(espacio,subArbol.getDato())
            self.mostrar(subArbol.getIzquierdo(),espacio+"   ")
    

if __name__ == '__main__':
    abb = ArbolBinarioBusqueda()
    abb.insertar(abb.getRaiz(),10)
    abb.insertar(abb.getRaiz(),5)
    abb.insertar(abb.getRaiz(),5)
    abb.insertar(abb.getRaiz(),15)
    abb.insertar(abb.getRaiz(),3)
    abb.insertar(abb.getRaiz(),7)
    abb.insertar(abb.getRaiz(),12)
    abb.insertar(abb.getRaiz(),17)
    

    abb.mostrar(abb.getRaiz(),"")