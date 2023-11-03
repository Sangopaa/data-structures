from .classes.class_stack import Stack

def viewIsBalanced(value_verify):
    print('Is balanced?: ', isBalanced(value_verify))
    raise
    
def decide_exercise(exercise:int) -> int:
    if exercise == 1:
        print('Valores permitidos [] {} ()')
        value = input()
        viewIsBalanced(value)
        


def run_exercises():
    # Llama a una función del archivo importado
    print('EXERCISES OF STACKS\n\n')
    
    activate_console = True
    
    while activate_console == True:
        print("""\n1. Dada una cadena que contiene paréntesis (), corchetes [] y llaves {}, tu tarea es determinar si la expresión está balanceada. Una expresión se considera balanceada si cada paréntesis, corchete y llave se abre y se cierra en el orden correcto y no hay elementos sobrantes o mal emparejados.""")
        
        input_value = int(input())
        
        decide_exercise(input_value)
    
    
def isBalanced(values_verify):
    stack = Stack()
    balanced = True
    
    values_expected = ['[', ']', '{', '}', '(', ')']
    aperture_values = ['[', '{', '(']
    closing_values = [']', '}', ')']
    
    for value in values_verify:
        if value in values_expected and value in closing_values:
            if stack.Size() == 0:
                balanced = False
                break
            
            if stack.Peek() == aperture_values[0] and value == closing_values[0]:
                stack.Pop()
            
            elif stack.Peek() == aperture_values[1] and value == [1]:
                stack.Pop()
            
            elif stack.Peek() == aperture_values[2] and value == [2]:
                stack.Pop()
                
            else:
                balanced = False
                break
                
        if value in values_expected and value in aperture_values:
            stack.Push(value)
            
    if not stack.isEmpty():
        balanced = False
            
    return balanced