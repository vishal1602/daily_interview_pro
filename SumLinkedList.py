"""
You are given two linked-lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode(object):
	def __init__(self, x):
		self.val=x
		self.next=None


class Solution:
	def addTwoNumbers(self, l1, l2, c=0, sum=[]):
		if l1 and l2:
			temp_sum = l1.val + l2.val + c
			if temp_sum > 9:
				sum.append(int(str(temp_sum)[1:]))
				c = int(str(temp_sum)[:1])
			else:
				sum.append(temp_sum)
				c=0
			sum = self.addTwoNumbers(l1.next, l2.next, c, sum=sum)
		elif l1:
			sum.append(l1.val+c)
			sum = self.addTwoNumbers(l1.next, None, sum=sum)
		elif l2:
			sum.append(l2.val+c)
			sum = self.addTwoNumbers(lNone, l2.next, sum=sum)
		return sum


l1 = ListNode(5)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
print(result)