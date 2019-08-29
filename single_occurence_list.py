# Given a list of numbers, where every number shows up twice except for one number, find that one number.

def singleNumber(nums):
	for num in nums:
		nums.remove(num)
		if num not in nums:
			return num
	return None
  	

print (singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1