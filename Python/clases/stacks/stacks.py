from ..nodo_clase import NodeStack

class Stack:
    def __init__(self) -> None:
        self.head = None
        self.length = 0
        
    def __str__(self) -> str:
        valores = []
        nodo_actual = self.head
        
        while nodo_actual:
            valores.append(str(nodo_actual.valor))
            nodo_actual = nodo_actual.siguiente
            
        return "[" + ", ".join(valores) + "]"
    
    def Push(self, value):
        new_node = NodeStack(value)
        new_node.siguiente = self.head
        self.head = new_node
        self.length += 1
        
    def Pop(self):
        return_value = self.head.value
        self.head = self.head.siguiente
        self.length -= 1
        
        return return_value
    
    def Peek(self):
        return_value = None
        if self.head:
            return_value = self.head.value
            
        return return_value
        
    def isEmpty(self):
        return self.head is None
    
    def Size(self):
        return self.length
            