# Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2
import itertools

def findPythagoreanTriplets(nums):
	for prod in itertools.permutations(nums, 3):
		if prod[0]**2 + prod[1]**2 == prod[2]**2:
			return True
	return False

print (findPythagoreanTriplets([3, 12, 5, 13]))
# True
