from linked_list import LinkedList

my_tasks = [{'name_task': 'task one', 'status': 'pending'}, 
            {'name_task': 'task two', 'status': 'pending'}, 
            {'name_task': 'task three', 'status': 'pending'}]


my_linked_list = LinkedList()    
    
def addItem(element):
    my_linked_list.push(element)
