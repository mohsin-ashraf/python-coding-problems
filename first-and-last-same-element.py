
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""


def binary_search(_list,target):
	left = 0
	right = len(_list) -1
	mid = (left + right) // 2
	while (left < right):
		print ( mid)
		if _list[mid] == target:
			return mid
		elif _list[mid] > target:
			right = mid - 1
		else:
			left = mid + 1
	return -1


def get_first_last(_list,target):
	index = binary_search(_list,target)
	if index == -1:
		return -1
	first = -1
	last = -1
	while (_list[index - 1] == target):
		first = index - 1
		index -= 1

	while (_list[index + 1] == target):
		last = index + 1
		index += 1
	return first,last


if __name__ == "__main__":
	_list = [1,2,3,4,5,11,11,11,23,45,67,88,99]
	target = 11
	first,last = get_first_last(_list,target)
	print (f"In {_list} the first occurence of {target} is: {first} and the last is: {last}")