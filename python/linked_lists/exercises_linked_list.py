from .classes.class_linked_list import LinkedList

def run_exercises():
    activate_console = True
    
    while activate_console == True:
        print("""\n1. Exercises ONE.
            \n2. Exercises TWO.
            \n3. Exercises THREE""")
        
        input_value = int(input())