from .class_node import NodeStack

class Stack:
    def __init__(self) -> None:
        self.head = None
        self.length = 0
        
    def __str__(self) -> str:
        values = []
        current_node = self.head
        
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.siguiente
            
        return "[" + ", ".join(values) + "]"
    
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
            