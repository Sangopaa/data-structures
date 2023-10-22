class Nodo:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.siguiente = None
        
class ListaEnlazada:
    def __init__(self) -> None:
        self.cabeza = None
        
    def push(self, valor)-> None:
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        
    def append(self, valor)-> None:
        nuevo_nodo = Nodo(valor)

        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza

            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            
            nodo_actual.siguiente = nuevo_nodo
    
    def insert(self, valor, posicion):
        nuevo_nodo = Nodo(valor)
        
        if posicion == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            contador = 0
            while contador < posicion - 1 and nodo_actual:
                nodo_actual = nodo_actual.siguiente
                contador += 1

            if nodo_actual is None:
                raise IndexError("Posición fuera de rango")
            nuevo_nodo.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

            
    
    def removeLast(self)-> None:
        if self.cabeza:
            if not self.cabeza.siguiente:
                self.cabeza = None
            else:
                nodo_actual = self.cabeza
                while nodo_actual.siguiente.siguiente:
                    nodo_actual = nodo_actual.siguiente
                
                nodo_actual.siguiente = None
                
    def pop(self)-> None:
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente
            
    def invertList(self):
        nodo_anterior = None
        nodo_actual = self.cabeza
        
        while nodo_actual:
            siguiente_nodo = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_anterior
            nodo_anterior = nodo_actual
            nodo_actual = siguiente_nodo
        
        self.cabeza = nodo_anterior
        
    def printList(self)-> None:
        nodo_actual = self.cabeza
        
        while nodo_actual:
            print(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

mi_lista = ListaEnlazada()

# Agregar elementos al principio (push)
mi_lista.append(1)
mi_lista.append(2)
mi_lista.append(3)



mi_lista.printList()
print('--------------------------')
mi_lista.invertList()
mi_lista.printList()




    
    
