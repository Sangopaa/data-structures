from ..nodo_clase import NodoDoble

class ListaDoblementeEnlazada:
    def __init__(self) -> None:
        self.cabeza = None
        
    def __str__(self) -> str:
        valores = []
        nodo_actual = self.cabeza
        
        while nodo_actual:
            valores.append(str(nodo_actual.valor))
            nodo_actual = nodo_actual.siguiente
            
        return "[" + ", ".join(valores) + "]"
    
    def push(self, valor) -> None:
        nuevo_nodo = NodoDoble(valor)
        nuevo_nodo.anterior = None
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        
        
        