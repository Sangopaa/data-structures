from clases.stacks.stacks import Stack

stack = Stack()

values_expected = ['[', ']', '{', '}', '(', ')']
aperture_values = ['[', '{', '(']
closing_values = [']', '}', ')']
values_verify = '[]'

balanced = True

for value in values_verify:
    if value in values_expected:
        if value in closing_values:
            if stack.Size() == 0:
               balanced = False
        
        if value in aperture_values:
            stack.Push(value)
             
    else:
        print('no esta')