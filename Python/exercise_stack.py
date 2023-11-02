from clases.stacks.stacks import Stack

stack = Stack()

values_verify = '[[]'
    
def isBalanced(values_verify):
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
        
        if value not in values_expected:
            print('Caracter no reconocido')
            
    if not stack.isEmpty():
        balanced = False
            
    return balanced
            
print(isBalanced(values_verify))