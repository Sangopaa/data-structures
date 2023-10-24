#Clase de lista simplemente enlazada
from clases.lista_enlazada.clase_lista_enlazada import ListaEnlazada

mi_lista = ListaEnlazada()

# Agregar elementos al principio (push)
mi_lista.append('holaa')
mi_lista.append('como')
mi_lista.append('estaaas')

print(mi_lista)
mi_lista.invertList()
print(mi_lista)

print('----------------------------------')
#-------------------------------------------------------------------------

#Clase de lista doblemente enlazada
from clases.lista_doblemente_enlazada.clase_lista_doblemente_enlazada import ListaDoblementeEnlazada

lista_doble = ListaDoblementeEnlazada()

lista_doble.push('holaa')

print(lista_doble)


    
