class Nodo:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.siguiente = None
        
class NodoDoble:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.siguiente = None
        self.anterior = None
        
class NodoQueue:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.siguiente = None
        