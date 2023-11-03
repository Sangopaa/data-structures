from .class_node import Node
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def __str__(self) -> str:
        values = []
        current_node = self.head
        
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
            
        return "[" + ", ".join(values) + "]"
        
    def push(self, value)-> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def append(self, value)-> None:
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current_node = self.head

            while current_node.next:
                current_node = current_node.next
            
            current_node.next = new_node
    
    def insert(self, value, position):
        new_node = Node(value)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            counter = 0
            while counter < position - 1 and current_node:
                current_node = current_node.next
                counter += 1

            if current_node is None:
                raise IndexError("Posición fuera de rango")
            new_node.next = current_node.next
            current_node.next = new_node

            
    
    def removeLast(self)-> None:
        if self.head:
            if not self.head.next:
                self.head = None
            else:
                current_node = self.head
                while current_node.next.next:
                    current_node = current_node.next
                
                current_node.next = None
                
    def pop(self)-> None:
        if self.head:
            self.head = self.head.next
            
    def invertList(self):
        previus_node = None
        current_node = self.head
        
        while current_node:
            next_node = current_node.next
            current_node.next = previus_node
            previus_node = current_node
            current_node = next_node
        
        self.head = previus_node