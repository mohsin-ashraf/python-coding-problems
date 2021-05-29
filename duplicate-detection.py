"""
Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

def contains_duplicates_1(_list):
	return len(_list) != len(set(_list))

def contains_duplicates_2(_list):
	dictionary = {}
	for element in _list:
		if element in dictionary:
			return True
		dictionary[element] = element
	return False


if __name__ == "__main__":

	list_1 = [1,1,1,3,3,4,3,2,4,2]
	list_2 = [1,2,3,4,5,6,7]

	print (f"{list_1} contains duplicates: {contains_duplicates_1(list_1)}")
	print (f"{list_1} contains duplicates: {contains_duplicates_2(list_1)}")


	print (f"{list_2} contains duplicates: {contains_duplicates_1(list_2)}")
	print (f"{list_2} contains duplicates: {contains_duplicates_2(list_2)}")