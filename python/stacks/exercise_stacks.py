from .classes.class_stack import Stack

def run_exercises():
    # Llama a una función del archivo importado
    print('Exercises of Stacks')
    
    print('esta balanceada la expresion?: ', isBalanced('[]'))
    
    
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