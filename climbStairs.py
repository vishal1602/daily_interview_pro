# You are given a positive integer N which represents the number of steps in a staircase. 
# You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.
import itertools

def staircase(n):
	count = 0
	for i in range(1,n+1):
		for l in itertools.product([1,2],repeat=i):
			#print(l)
			if sum(l) == n:
				count+=1
	return count

  
print (staircase(4))
# 5
print (staircase(5))
# 8