"""
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

def two_numbers_sum_1(_list, target):
	dictionary = {y:x for (x,y) in enumerate(_list)}
	for number in _list:
		goal = target - number
		if goal in dictionary:
			return goal, number
	return None

def two_numbers_sum_2(_list, target):
	dictionary = {}
	for number in _list:
		goal = target - number
		if goal in dictionary:
			return [goal, number]
		dictionary[number] = True

if __name__ == "__main__":
	_list = [3,4,5,6,7,8]
	target = 15 
	print (two_numbers_sum_1(_list, target))
	print (two_numbers_sum_2(_list, target))
