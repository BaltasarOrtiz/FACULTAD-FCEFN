from arbolBB import ArbolBinarioBusqueda
import os

def menu():
    opc = int(input("""
Ingrese [1]: Mostrar el nodo padre y el nodo hermano
Ingrese [2]: Mostrar la cantidad de nodos del árbol en forma recursiva
Ingrese [3]: Mostrar la altura de un árbol
Ingrese [4]: Mostrar los sucesores de un nodo ingresado previamente por teclado
Ingrese [5]: Mostrar el árbol
Ingrese [6]: Salir
Ingrese Opcion-> """))
    return opc

if __name__ == "__main__":
    os.system("cls")
    abb= ArbolBinarioBusqueda()
    abb.insertar(5)
    abb.insertar(3)
    abb.insertar(2)
    abb.insertar(4)
    abb.insertar(7)
    abb.insertar(6)
    abb.insertar(8)
    

    bandera= True

    while bandera:
        opc= menu()
        if opc==1:
            dato= int(input("Ingrese el valor del Nodo: "))
            padre = abb.getPadre(dato)
            hermano = abb.getHermano(dato, padre)

            if padre != None:
                if hermano != None:
                    hermano = hermano.getDato()
                else:
                    hermano = "Ninguno"

                print("El padre del nodo es: ",padre.getDato(), " y el hermano es: ", hermano)
            else:
                print("El nodo no existe")

        elif opc==2:
            print("La cantidad de nodos del árbol es: ", abb.contador())

        elif opc==3:
            print("La altura del árbol es: ", abb.altura())

        elif opc==4:
            dato= int(input("Ingrese el dato a buscar: "))
            abb.mostrarSucesores(dato)
            
        elif opc==5:
            abb.mostrarArbolBin()
        
        elif opc==6:
            bandera= False

        else:
            print("Opción no válida")
    
"""
a) Mostrar el nodo padre y el nodo hermano, de un nodo previamente ingresado por teclado; éste puede o no 
existir en el árbol. 
b) Mostrar la cantidad de nodos del árbol en forma recursiva. 
c) Mostrar la altura de un árbol. 
d) Mostrar los sucesores de un nodo ingresado previamente por teclado
"""
    