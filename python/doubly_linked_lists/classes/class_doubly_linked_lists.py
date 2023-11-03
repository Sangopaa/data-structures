from .class_node import Node

class ListaDoblementeEnlazada:
    def __init__(self) -> None:
        self.head = None
        
    def __str__(self) -> str:
        values = []
        current_node = self.head
        
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
            
        return "[" + ", ".join(values) + "]"
    
    def push(self, value) -> None:
        new_node = Node(value)
        new_node.before = None
        new_node.next = self.head
        self.head = new_node
        
        
        