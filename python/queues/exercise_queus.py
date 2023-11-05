from .classes.class_queu import Queue

def order_clients(number_clients:int):
    my_queue = Queue()
    timer = 0
    order_service = []
    
    info_clients = []
    
    for client in range(number_clients):
        identifier = int(input('Please enter the customer identifier: '))
        waiting_time = int(input('Please enter the customer is waiting time: '))

        temporal_client = {'identifier': identifier, 'time': waiting_time}
        info_clients.append(temporal_client)

    for client in info_clients:
        my_queue.Enqueue(client)
        
    while not my_queue.IsEmpty():
        client = my_queue.Front()
        timer += client['time']
        order_service.append(client['identifier'])
        my_queue.Dequeue()
        
    print('Atention time: ', timer)
    print('Order customers: ', order_service)
    raise
    

def decide_exercise(exercise:int) -> int:
    if exercise == 1:
        value = int(input('Please enter the number of clients you wish serve: '))
        order_clients(value)
        

def run_exercises():
    print('\nEXERCISES OF QUEUES\n\n')

    active_console = True
    
    while active_console == True:        
        input_value = int(input("""\n1. En una oficina de atención al cliente, los clientes llegan en orden y se unen a una cola para recibir atención. Cada cliente tiene una cierta cantidad de tiempo requerido para ser atendido. Sin embargo, debido a la limitación de recursos, solo se pueden atender a ciertos clientes al mismo tiempo. La cola debe procesarse en orden, y no se puede atender a un cliente posterior hasta que se haya completado la atención del cliente actual. Tu tarea es determinar el orden en el que se atienden a los clientes y cuánto tiempo debe esperar cada cliente para ser atendido.\n\n RESPONSE: """))
        decide_exercise(input_value)


