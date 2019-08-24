# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

def sortNums(nums):
  stack = []
  dic = {}
  min_num = min(nums)
  max_num = max(nums)
  for num in nums:
  	if num not in dic.keys():
  		dic[num] = 1
  	else:
  		dic[num] = dic[num]+1
  	if (num != max_num) & (num != min_num):
  		middle_num = num
  		
  stack.extend([min_num]*dic[min_num])
  stack.extend([middle_num]*dic[middle_num])
  stack.extend([max_num]*dic[max_num])

  return stack

print (sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
