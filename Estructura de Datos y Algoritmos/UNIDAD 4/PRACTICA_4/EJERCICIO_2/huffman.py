from nodo import Nodo

class Huffman:
    __cabeza : None|Nodo 

    def __init__(self):
        self.__cabeza = None 
    
    def vacio(self):
        return self.__cabeza == None
    
    def insertar(self, letra, frecuencia):
        nuevoNodo = Nodo(key, frecuencia)
        
        if self.vacio():
            self.__cabeza = nuevoNodo
        else:
            aux = self.__cabeza
            
            while aux.getSiguiente() != None: #type: ignore
                aux = aux.getSiguiente() #type: ignore
            
            aux.setSiguiente(nuevoNodo) #type: ignore

    def mostrar(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getLetra(), aux.getFrecuencia())
            aux = aux.getSiguiente() #type: ignore
        
    def codificador(self):
        pass


if __name__ == "__main__":
    dic ={  "A" : 15, 
            "B" : 6, 
            "C" : 7, 
            "D" : 12, 
            "E" : 25, 
            "F" : 4,
            "G" : 6,
            "H" : 1,
            "I" : 15, }

    h = Huffman()

    for key in dic:
        h.insertar(key, dic[key])

    h.mostrar()