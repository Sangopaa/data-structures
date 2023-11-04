from class_queue import Queue

my_queue = Queue()
timer = 0
order_service = []

info_clients = [{'identifier': 3, 'time': 2},
                {'identifier': 1, 'time': 1},
                {'identifier': 2, 'time': 3}]

for client in info_clients:
    my_queue.Enqueue(client)
    
while not my_queue.IsEmpty():
    client = my_queue.Front()
    timer += client['time']
    order_service.append(client['identifier'])
    my_queue.Dequeue()

print(timer)
print(order_service)