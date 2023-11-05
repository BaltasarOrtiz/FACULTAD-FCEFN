from nodo import Nodo
import os

class ArbolBinarioBusqueda:
    __raiz : Nodo|None
    __cantidad : int
   
    def __init__(self):
        self.__raiz = None #type: ignore
        self.__cantidad = 0

    def vacio(self):
        return self.__raiz == None
    
    def insertar(self, dato):                               
        if self.vacio():                                        
            self.__raiz = Nodo(dato)
            self.__cantidad += 1
        else:                                                   
            self.insertarOtro(self.__raiz, dato)
        
    def insertarOtro(self, subArbol, dato): 
        if dato == subArbol.getDato():
            return None
        else:
            if dato < subArbol.getDato():                           
                if subArbol.getIzquierdo() == None:                     
                    subArbol.setIzquierdo(Nodo(dato))
                else:                                               
                    self.insertarOtro(subArbol.getIzquierdo(), dato)

            elif dato > subArbol.getDato():                     
                if subArbol.getDerecho() == None:
                    subArbol.setDerecho(Nodo(dato))
                else:
                    self.insertarOtro(subArbol.getDerecho(), dato)
            self.__cantidad += 1
    
    def buscar(self, dato):
        aux = self.__raiz
        while aux != None and aux.getDato() != dato:
            if dato < aux.getDato():
                aux = aux.getIzquierdo()
            else:
                aux = aux.getDerecho()
        return aux
    #hacer un buscar

    def buscarRecursivo(self, subArbol, dato):
        if subArbol == None:
            return None
        elif dato == subArbol.getDato():
            return subArbol
        elif dato < subArbol.getDato():
            return self.buscarRecursivo(subArbol.getIzquierdo(), dato)
        else:
            return self.buscarRecursivo(subArbol.getDerecho(), dato)

    
    def suprimir(self, dato):
        if self.vacio():                            
            print ("Arbol vacio")
        else:                                       
            self.suprimirOtro(self.__raiz, self.__raiz, dato)
            
    def suprimirOtro(self, subArbol, anterior, dato):
        if dato < subArbol.getDato():                                                         
            self.suprimirOtro(subArbol.getIzquierdo(), subArbol, dato)                              
        elif dato > subArbol.getDato():                                                       
            self.suprimirOtro(subArbol.getDerecho(), subArbol, dato)                                
        elif subArbol.getDato() == None:                                                       
            return print("El dato no existe")                                                     
        else:                                                                                 
            if subArbol.getIzquierdo() == None and subArbol.getDerecho() == None:                   
                if anterior.getIzquierdo() == subArbol:                                                 
                    anterior.setIzquierdo(None)                                                             
                else:                                                                                   
                    anterior.setDerecho(None)                                                               
            elif subArbol.getIzquierdo() == None:                                                   
                if anterior.getIzquierdo() == subArbol:                                                 
                    anterior.setIzquierdo(subArbol.getDerecho())                                            
                else:                                                                                  
                    anterior.setDerecho(subArbol.getDerecho())                                              
            elif subArbol.getDerecho() == None:                                                     
                if anterior.getIzquierdo() == subArbol:                                                 
                    anterior.setIzquierdo(subArbol.getIzquierdo())                                         
                else:                                                                                  
                    anterior.setDerecho(subArbol.getIzquierdo())                                            
            else:                                                                                   
                aux = subArbol.getIzquierdo()                                                            
                padreAux = subArbol                                                                      
                while aux.getDerecho() != None:                                                          
                    padreAux = aux                                                                       
                    aux = aux.getDerecho()                                                               
                subArbol.setDato(aux.getDato())                                                          
                if padreAux == subArbol:                                                                 
                    padreAux.setIzquierdo(aux.getIzquierdo())                                            
                else:                                                                                    
                    padreAux.setDerecho(aux.getIzquierdo())                                             
            self.__cantidad -= 1                                                 

    def camino(self, dato_desde, dato_hasta): #modificar 
        desde= self.buscar(dato_desde)
        hasta= dato_hasta

        while desde != None and desde.getDato() != hasta:
            if hasta < desde.getDato():
                desde = desde.getIzquierdo()
            else:
                desde = desde.getDerecho()

        if desde != None:
            return True
        else: 
            return False

    def mayor(self):
        aux = self.__raiz
        while aux.getDerecho() != None: # type: ignore
            aux = aux.getDerecho() # type: ignore
        return aux
        
    def nivel(self, dato):
        aux = self.__raiz
        nivel = 0
        while aux != None and aux.getDato() != dato:
            if dato < aux.getDato():
                aux = aux.getIzquierdo()
            else:
                aux = aux.getDerecho()
            nivel += 1
            
        if aux == None:
            return -1
        else:
            return nivel
        
    def hijo(self, datoPadre, datoHijo):
        nodoPadre = self.buscar(datoPadre)

        if nodoPadre == None:
            return False
        else:
            if nodoPadre.getIzquierdo() != None and nodoPadre.getIzq().getDato() == datoHijo: # type: ignore
                return True
            elif nodoPadre.getDer() != None and nodoPadre.getDer().getDato() == datoHijo: # type: ignore
                return True
            else:
                return False

    def padre(self, datoHijo, datoPadre):
        return self.hijo(datoPadre, datoHijo)
      
    def hoja(self, dato):
        aux = self.buscar(dato)

        if aux == None:
            return False
        else:
            return aux.getIzquierdo() == None and aux.getDerecho() == None
        
    def preOrden(self, subArbol):
        if subArbol!=None:
            print(subArbol.getDato())
            self.preOrden(subArbol.getIzquierdo())
            self.preOrden(subArbol.getDerecho())
    
    def inOrden(self, subArbol):
        if subArbol!=None:
            self.inOrden(subArbol.getIzquierdo())
            print(subArbol.getDato())
            self.inOrden(subArbol.getDerecho())
    
    def postOrden(self, subArbol):
        if subArbol!=None:
            self.postOrden(subArbol.getIzquierdo())
            self.postOrden(subArbol.getDerecho())
            print(subArbol.getDato())

#---Otros Metodos:  Mostrar---#
    def mostrarArbolBin(self, sangria=4):
        if self.__raiz == None:
            print("El arbol esta vacio")
            return

        def mostrarArbolBinRec(nodo, cadena):
            print(str(nodo.getDato()))
            #Para el hijo derecho
            if nodo.getDerecho() != None:
                if nodo.getIzquierdo() != None:
                    print(cadena+ "├" + "─" * sangria, end="") 
                else:
                    print(cadena+ "└" + "─" * sangria, end="")
                mostrarArbolBinRec(nodo.getDerecho(), cadena + "│" + " " *sangria)
            #Para el hijo izquierdo
            if nodo.getIzquierdo() != None:
                print(cadena+ "└" + "─" * sangria, end="")
                mostrarArbolBinRec(nodo.getIzquierdo(), cadena + " " *sangria)

        mostrarArbolBinRec(self.__raiz, "")

    def antecesoresIterativo(self, dato):
        subArbol = self.__raiz
        if subArbol != None:
            antecesores = []
            if subArbol.getDato() != dato:
                antecesores.append(subArbol.getDato())
                if subArbol.getDato() > dato:
                    subArbol = subArbol.getIzquierdo()
                else:
                    subArbol = subArbol.getDerecho()
                while subArbol != None and subArbol.getDato() != dato:
                    antecesores.append(subArbol.getDato())
                    if subArbol.getDato() > dato:
                        subArbol = subArbol.getIzquierdo()
                    else:
                        subArbol = subArbol.getDerecho()
                
                return antecesores
        else:
            print("El arbol no existe")

    def antecesores(self, dato):
        lista=[]
        return self.antecesoresRecursivo(self.__raiz, dato, lista)

    def antecesoresRecursivo(self, subArbol, dato, lista):
        if subArbol != None:
            if subArbol.getDato() != dato:
                lista.append(subArbol.getDato())
                if subArbol.getDato() > dato:
                    self.antecesoresRecursivo(subArbol.getIzquierdo(), dato, lista)
                else:
                    self.antecesoresRecursivo(subArbol.getDerecho(), dato, lista)
            return lista
        
if __name__ == '__main__':
    os.system("cls")
    abb = ArbolBinarioBusqueda()
    abb.insertar(5)
    abb.insertar(3)
    abb.insertar(7)
    abb.insertar(14)

    print("Antecesores de 14: ", abb.antecesoresIterativo(14))
    print("Antecesores de 14: ", abb.antecesores(14))



