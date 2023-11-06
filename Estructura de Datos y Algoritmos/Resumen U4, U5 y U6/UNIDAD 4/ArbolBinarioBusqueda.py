from Nodo_ABB import Nodo

class ArbolBinarioBusqueda:
    __raiz : Nodo|None
    __cantidad : int
   
    def __init__(self):
        self.__raiz = None #type: ignore
        self.__cantidad = 0

    def vacio(self):
        return self.__cantidad == 0
    
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

    def buscarRecursivo(self, subArbol, dato):
        if subArbol == None:
            return None
        elif dato == subArbol.getDato():
            return subArbol
        elif dato < subArbol.getDato():
            return self.buscarRecursivo(subArbol.getIzquierdo(), dato)
        else:
            return self.buscarRecursivo(subArbol.getDerecho(), dato)                  

    def camino(self, dato_desde, dato_hasta):
        desde = self.buscar(dato_desde)
        hasta = dato_hasta

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

    def grado(self, dato):
        aux = self.buscar(dato)

        if aux == None:
            return -1
        else:
            if aux.getIzquierdo() != None and aux.getDerecho() != None:
                return 2
            elif aux.getIzquierdo() != None or aux.getDerecho() != None:
                return 1
            else:
                return 0

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

    def padre(self, datoPadre, datoHijo):
        return self.hijo(datoPadre, datoHijo)
      
    def hoja(self, dato):
        aux = self.buscar(dato)

        if aux == None:
            return False
        else:
            return aux.getIzquierdo() == None and aux.getDerecho() == None

#--------------------- Métodos de Recorrido ---------------------   
    def prO(self):
        self.preOrden(self.__raiz) #<-- preguntar
    
    def iO(self):
        self.preOrden(self.__raiz) #<-- preguntar

    def poO(self):
        self.preOrden(self.__raiz)  #<-- preguntar 

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

#--------------------- Otros Metodos ---------------------

    def frontera(self):
        lista = []
        if self.__raiz == None:
            print("El arbol esta vacio")
        else:
            self.fronteraRec(self.__raiz, lista)
            return lista
        
    def fronteraRec(self, nodo, lista):
        if nodo != None:
            if nodo.getIzquierdo() == None and nodo.getDerecho() == None:
                lista.append(nodo.getDato())
            else:
                self.fronteraRec(nodo.getIzquierdo(), lista)
                self.fronteraRec(nodo.getDerecho(), lista)

    def getPadre(self, dato):
        aux = self.__raiz
        padre = None
        while aux != None and aux.getDato() != dato:
            padre = aux
            if dato < aux.getDato():
                aux = aux.getIzquierdo()
            else:
                aux = aux.getDerecho()
        return padre
        
    def getHermano(self, dato, padre):
        if padre != None:
            if dato < padre.getDato():
                return padre.getDerecho()
            else:
                return padre.getIzquierdo()
        
    def contador(self):
        if self.__raiz == None:
            print("El arbol esta vacio")
        else:
            cont = self.contadorRecursivo(self.__raiz,0)
            return cont
        
    def contadorRecursivo(self, subArbol, cont):
        if subArbol != None:
            cont=self.contadorRecursivo(subArbol.getIzquierdo(),cont)
            cont=self.contadorRecursivo(subArbol.getDerecho(),cont)
            cont+=1

        return cont

    def altura(self):
        if self.__raiz == None:
            print("El arbol esta vacio")
        else:
            return self.alturaRecursivo(self.__raiz)
    
    def alturaRecursivo(self, subArbol):
        if subArbol == None:
            return -1
        else:
            altIzq = self.alturaRecursivo(subArbol.getIzquierdo())
            altDer = self.alturaRecursivo(subArbol.getDerecho()) 
            if altIzq > altDer:
                return altIzq + 1
            else:
                return altDer + 1

    def mostrarSucesores(self, dato):
        nodo = self.buscar(dato)
        if nodo != None:
            lista = []
            self.mostrarSucesoresRec(nodo,lista)
            lista.remove(dato)
            print("Los sucesores de ", dato, "son: ", lista)
        else:
            print("El dato no existe")

    def mostrarSucesoresRec(self, nodo, lista):
        if nodo != None:
            lista.append(nodo.getDato())
            self.mostrarSucesoresRec(nodo.getIzquierdo(),lista)
            self.mostrarSucesoresRec(nodo.getDerecho(),lista)


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