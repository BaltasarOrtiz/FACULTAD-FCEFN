from arbolBB import ArbolBinarioBusqueda
import os

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
    abb.mostrarArbolBin()
    
    frontera=[]

    abb.frontera(frontera)
    print("\nLa frontera del arbol es: ", frontera)