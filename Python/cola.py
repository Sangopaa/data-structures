from clases.colas.cola import Cola

mi_cola = Cola()

mi_cola.Encolar('hola')
mi_cola.Encolar('como estas')
mi_cola.Encolar('7w7')

valor_desencolar = mi_cola.ValorDesencolar()
print(valor_desencolar)
print(mi_cola)
mi_cola.Desencolar()

print(mi_cola)