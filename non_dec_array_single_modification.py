# You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.

# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

def check(lst):
  min_val = min(lst)
  num_changes = 0
  for i in range(0, len(lst) - 1):
  	if lst[i] < lst[i+1]:
  		pass
  	elif lst[i] <= min_val:
  		return False
  	else:
  		num_changes += 1
  return (num_changes == 1) | (num_changes == 0)

print (check([13, 4, 7]))
# True
print (check([5,1,3,2,5]))
# False
print (check([1, 4, 7]))
# True
