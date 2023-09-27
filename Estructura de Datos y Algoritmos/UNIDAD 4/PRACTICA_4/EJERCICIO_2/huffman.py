from nodo import Nodo
import os

class Huffman:
    __cabeza : None|Nodo 

    def __init__(self):
        self.__cabeza = None 
    
    def vacio(self):
        return self.__cabeza == None
    
    def insertar(self, letra, frecuencia):
        nuevoNodo = Nodo(letra, frecuencia)
        
        if self.vacio() or frecuencia < self.__cabeza.getFrecuencia(): #type: ignore
            nuevoNodo.setSiguiente(self.__cabeza)
            self.__cabeza = nuevoNodo
        else:
            aux = self.__cabeza
            anterior = None
            
            while aux is not None and frecuencia > aux.getFrecuencia():
                anterior = aux
                aux = aux.getSiguiente()

            nuevoNodo.setSiguiente(aux)
            anterior.setSiguiente(nuevoNodo) #type: ignore
    
    def insertarOtro(self, letra, frecuencia, izquierdo, derecho):
        nuevoNodo = Nodo(letra, frecuencia)
        nuevoNodo.setIzquierdo(izquierdo)
        nuevoNodo.setDerecho(derecho)
        
        if self.vacio() or frecuencia < self.__cabeza.getFrecuencia(): #type: ignore
            nuevoNodo.setSiguiente(self.__cabeza)
            self.__cabeza = nuevoNodo
        else:
            aux = self.__cabeza
            anterior = None
            
            while aux is not None and frecuencia > aux.getFrecuencia():
                anterior = aux
                aux = aux.getSiguiente()

            nuevoNodo.setSiguiente(aux)
            anterior.setSiguiente(nuevoNodo) #type: ignore

    def suprimir(self):
        if self.vacio():
            print("No hay elementos en la lista")
        else:
            aux = self.__cabeza
            self.__cabeza = self.__cabeza.getSiguiente()
            aux.setSiguiente(None)
            return aux
    
    def generarSubarbol(self):
        while self.__cabeza.getSiguiente() != None:
            nodo1 = self.suprimir()
            nodo2 = self.suprimir()

            frecuencia = nodo1.getFrecuencia() + nodo2.getFrecuencia() #type: ignore
            letra = nodo1.getLetra() + nodo2.getLetra() #type: ignore
            #print(letra, frecuencia)

            izquierdo = nodo1
            derecho = nodo2
        
            self.insertarOtro(letra, frecuencia, izquierdo, derecho)

#Metodos para codificar en binario
    def mostrarTabla(self, tabla):
        print("Letra | Codigo")
        for i in tabla:
            print(i[0], "   |", i[1])
             
    def codificador(self):
        if self.vacio():
            print("El arbol esta vacio")
        else:
            tabla = []
            self.codificadorRec(self.__cabeza, "",tabla)  
            self.mostrarTabla(tabla=sorted(tabla, key=lambda x: len(x[1]), reverse=True))

    def codificadorRec(self, nodo, cadena,tabla):
        if nodo.getIzquierdo() == None and nodo.getDerecho() == None:
            tabla.append([nodo.getLetra(), cadena])
            return
        self.codificadorRec(nodo.getIzquierdo(), cadena + "0", tabla)
        self.codificadorRec(nodo.getDerecho(), cadena + "1", tabla)
            
#Metodos para mostrar el arbol
    def mostrarLista(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getLetra(), aux.getFrecuencia())
            aux = aux.getSiguiente()
    
    def mostrarArbolBin(self, sangria=4):
        if self.vacio():
            print("El arbol esta vacio")
            return

        def mostrarArbolBinRec(nodo, cadena):
            print(str(nodo.getLetra()+" -> [{}]".format(nodo.getFrecuencia())))
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

        mostrarArbolBinRec(self.__cabeza, "")
              
if __name__ == "__main__":
    os.system("cls")

    dic ={  "I" : 15, 
            "G" : 6, 
            "C" : 7, 
            "D" : 12, 
            "E" : 25, 
            "F" : 4,
            "B" : 6,
            "H" : 1,
            "A" : 15, }

    h = Huffman()
    
    for key in dic:
        h.insertar(key, dic[key])

    #h.mostrarLista()
    h.generarSubarbol()
    h.mostrarArbolBin()
    h.codificador()