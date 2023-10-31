from ..nodo_clase import Nodo
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def __str__(self) -> str:
        values = []
        current_node = self.head
        
        while current_node:
            values.append(str(current_node.valor))
            current_node = current_node.siguiente
            
        return "[" + ", ".join(values) + "]"
        
    def push(self, value)-> None:
        new_node = Nodo(value)
        new_node.siguiente = self.head
        self.head = new_node
        
    def append(self, value)-> None:
        new_node = Nodo(value)

        if not self.head:
            self.head = new_node
        else:
            current_node = self.head

            while current_node.siguiente:
                current_node = current_node.siguiente
            
            current_node.siguiente = new_node
    
    def insert(self, value, position):
        new_node = Nodo(value)
        
        if position == 0:
            new_node.siguiente = self.head
            self.head = new_node
        else:
            current_node = self.head
            counter = 0
            while counter < position - 1 and current_node:
                current_node = current_node.siguiente
                counter += 1

            if current_node is None:
                raise IndexError("Posición fuera de rango")
            new_node.siguiente = current_node.siguiente
            current_node.siguiente = new_node

            
    
    def removeLast(self)-> None:
        if self.head:
            if not self.head.siguiente:
                self.head = None
            else:
                current_node = self.head
                while current_node.siguiente.siguiente:
                    current_node = current_node.siguiente
                
                current_node.siguiente = None
                
    def pop(self)-> None:
        if self.head:
            self.head = self.head.siguiente
            
    def invertList(self):
        previus_node = None
        current_node = self.head
        
        while current_node:
            next_node = current_node.siguiente
            current_node.siguiente = previus_node
            previus_node = current_node
            current_node = next_node
        
        self.head = previus_node