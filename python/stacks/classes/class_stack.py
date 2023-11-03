from .class_node import Node

class Stack:
    def __init__(self) -> None:
        self.head = None
        self.length = 0
        
    def __str__(self) -> str:
        values = []
        current_node = self.head
        
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
            
        return "[" + ", ".join(values) + "]"
    
    def Push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        
    def Pop(self):
        output_value = self.head.value
        self.head = self.head.next
        self.length -= 1
        
        return output_value
    
    def Peek(self):
        output_value = None
        if self.head:
            output_value = self.head.value
            
        return output_value
        
    def isEmpty(self):
        return self.head is None
    
    def Size(self):
        return self.length
            