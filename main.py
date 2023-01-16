class Stack:
  def __init__(self):
    self.elements = []

  def push(self,data):
    self.elements.append(data)
    return data

  def pop(self):
    return self.elements.pop()

  def peek(self):
    return self.elements[-1]

  def is_empty(self):
    return len(self.elements) == 0

stack = Stack()
 # pushing the elements
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

 # again checking is_empty method -> false
print(stack.is_empty())

# printing the topmost element of the stack 
print(stack.peek())

# popping the topmost element 
stack.pop()

# checking the topmost element using peek method 
print(stack.peek())

# popping all the elements
stack.pop()
stack.pop() 
stack.pop() 
stack.pop() 

# checking the is_empty method for the last time 
print(stack.is_empty())