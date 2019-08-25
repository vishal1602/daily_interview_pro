# You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

# Example:
# Given [4, 7, 1 , -3, 2] and k = 5, 
# return true since 4 + 1 = 5.

def two_sum(list, k):
	for i in range(0, len(list)):
		if k - list[i] in list[i+1:]:
			return True
	return False

print (two_sum([4,7,1,-3,2], 5))
print (two_sum([5], 10))
