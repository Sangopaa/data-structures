from clases.stacks.stacks import Stack

my_stack = Stack()

print(my_stack.Size())

my_stack.Push('valor 1')
my_stack.Push('valor 2')
my_stack.Push('valor 3')
print(my_stack.Size())

value_stack = my_stack.Peek()
print(value_stack)

print(my_stack)