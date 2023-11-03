def linked_lists():
    #Import the function that executes the linked_lists exercises
    from linked_lists.exercises_linked_list import run_exercises as exercises_linked_lists
    
    try:
        #function that executes the linked lists exercises
        exercises_linked_lists()
    except:
        stop_console()

def queues():
    #Import the function that executes the queue exercises
    from queues.exercise_queus import run_exercises as execises_queues

    try:
        #function that executes the queue exercises
        execises_queues()
    except:
        print('Value Unexpected')
        stop_console()
    
def stacks():
    #Import the function that executes the stacks exercises
    from stacks.exercise_stacks import run_exercises as exercises_stacks
    
    try:
        #function that executes the stacks exercises
        exercises_stacks()
    except:
        print('Value Unexpected')
        stop_console()
    
def decide_data_structure(value: int) -> None | int:
    values_expected = [1, 2, 3]
    if value == values_expected[0]:
        linked_lists()

    if value == values_expected[1]:
        queues()
    
    if value == values_expected[2]:
        stacks()

    if value not in values_expected:
        print('Value Unexpected')
        stop_console()
    
def stop_console():
    global activate_console
    activate_console = False

activate_console = True

while activate_console == True:
    try:
        print("""\n1. Exercises of linked lists.
              \n2. Exercises of queues.
              \n3. Exercises of stacks.""")
        
        input_value = int(input())
        value_view = decide_data_structure(input_value)
    except:
        print('Value Unexpected')
        stop_console()

