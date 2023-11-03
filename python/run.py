import sys
import os

# Obtén la ruta del directorio actual (donde se encuentra ejecuta.py)
current_dir = os.path.dirname(__file__)

# Agrega el directorio raíz de tu proyecto a sys.path
root_dir = os.path.abspath(os.path.join(current_dir))
sys.path.append(root_dir)


#Importa la función que ejecuta los ejercicios de colas
from queues.exercise_queus import run_exercises as execises_queues

#Importa la función que ejecuta los ejercicios de pilas
from stacks.exercise_stacks import run_exercises as exercises_stacks

#Funcion que ejecuta los ejercicios de colas
execises_queues()

#Funcion que ejecuta los ejercicios de stacks
exercises_stacks()

