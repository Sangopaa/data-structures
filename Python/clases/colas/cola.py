from ..nodo_clase import NodoQueue

class Cola:
    def __init__(self) -> None:
        self.cabeza = None
        
    def __str__(self) -> str:
        valores = []
        nodo_actual = self.cabeza
        
        while nodo_actual:
            valores.append(str(nodo_actual.valor))
            nodo_actual = nodo_actual.siguiente
            
        return "[" + ", ".join(valores) + "]"
        
    def Encolar(self, valor):
        nuevoNodo = NodoQueue(valor)
        
        if not self.cabeza:
            self.cabeza = nuevoNodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
                
            nodo_actual.siguiente = nuevoNodo
            
    def Desencolar(self):
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente
            
    def ValorDesencolar(self)-> NodoQueue:
        nodo_saliente = None
        
        if self.cabeza:
            nodo_saliente = self.cabeza

        return nodo_saliente.valor
    

        
            
        
            
        