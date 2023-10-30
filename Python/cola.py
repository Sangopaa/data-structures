from clases.queues.queues import Queue

mi_cola = Queue() 
print(mi_cola.Longitud())
print('Valor a desencolar: ', mi_cola.ValorDesencolar())
mi_cola.Encolar('hola')
mi_cola.Encolar('como estas')
mi_cola.Encolar('7w7')
print('Valor a desencolar: ', mi_cola.ValorDesencolar())
print(mi_cola.Longitud())