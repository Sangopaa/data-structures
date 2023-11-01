from clases.queues.queues import Queue

my_queue = Queue() 
print(my_queue.Longitud())
print('Valor a desencolar: ', my_queue.ValorDesencolar())
my_queue.Encolar('hola')
my_queue.Encolar('como estas')
my_queue.Encolar('7w7')
print('Valor a desencolar: ', my_queue.ValorDesencolar())
print(my_queue.Longitud())