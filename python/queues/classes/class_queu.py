from .class_node import Node

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.final = None
        self.length = 0
        
    def __str__(self) -> str:
        values = []
        current_node = self.head
        
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
            
        return "[" + ", ".join(values) + "]"
        
    def Encolar(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.final = new_node
        else:
            self.final.next = new_node
            self.final = new_node
            
        self.length += 1
            
            
    def Desencolar(self):
        if self.head:
            self.head = self.head.next
            self.length -= 1
            
    def valueDesencolar(self):
        output_value = None
        if self.head:
            output_value = self.head.value

        return output_value
    
    def EstaVacia(self):
        output_value = True
        
        if self.head:
            output_value = False
            
        return output_value
    
    def length(self):
        return self.length        
        