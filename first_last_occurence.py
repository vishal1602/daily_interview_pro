class Solution: 
  def getRange(self, arr, target):
    len_arr = len(arr)
    first = last = -1
    for i in range(0, len_arr):
    	if (arr[i] == target) & (first == -1):
    		first = i

    	if (arr[len_arr-i-1] == target)  &  (last == -1):
    		last = len_arr-i-1

    return [first, last]
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))


arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 3
print(Solution().getRange(arr, x))