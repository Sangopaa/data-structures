from ..nodo_clase import NodoQueue

class Cola:
    def __init__(self) -> None:
        self.cabeza = None
        self.final = None
        self.longitud = 0
        
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
            self.final = nuevoNodo
        else:
            self.final.siguiente = nuevoNodo
            self.final = nuevoNodo
            
        self.longitud += 1
            
            
    def Desencolar(self):
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente
            self.longitud -= 1
            
    def ValorDesencolar(self):
        valor_saliente = None
        if self.cabeza:
            valor_saliente = self.cabeza.valor

        return valor_saliente
    
    def EstaVacia(self):
        valor_retoro = True
        
        if self.cabeza:
            valor_retoro = False
            
        return valor_retoro
    
    def Longitud(self):
        return self.longitud        
        
        
            
        
            
        