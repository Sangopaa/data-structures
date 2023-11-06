from linked_list import LinkedList

my_tasks = [{'name_task': 'task one', 'status': 'pending'}, 
            {'name_task': 'task two', 'status': 'pending'}, 
            {'name_task': 'task three', 'status': 'pending'}]


my_linked_list = LinkedList()

for element in my_tasks:
    my_linked_list.push(element)
    
print(my_linked_list)