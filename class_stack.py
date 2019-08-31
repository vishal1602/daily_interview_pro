# Implement a class for a stack that supports all the regular functions (push, pop) and an 
# additional function of max() which returns the maximum element in the stack 
# (return None if the stack is empty). Each method should run in constant time.


class MaxStack:
  def __init__(self):
  	self.items = []

  def push(self, val):
  	self.items.append(val)

  def pop(self):
  	self.items.pop()

  def max(self):
  	if not self.items:
  		return None
  	return max(self.items)

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print (s.max())
# 3
s.pop()
s.pop()
print (s.max())
# 2

p= MaxStack()
print (p.max())
#None