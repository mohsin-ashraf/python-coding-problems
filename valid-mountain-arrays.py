# Valid Mountain Arrays

"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
"""

def is_valid_mountain(list):
	if len(list) < 3:
		return False
	i = 1
	while (i < len(list) and list[i] > list[i - 1]):
		i += 1

	if i == 1 or i == len(list):
		return False

	while (i < len(list) and list[i] < list[i - 1]):
		i += 1

	if i == len(list):
		return True
	return False



def main():

	valid_mountain = [1,2,3,4,5,6,9,8,7,6,5,4,3,2,1]
	invalid_mountain = [1,2,3,4,5,6,5,4,3,4,5,6,7,8,]

	print (f"Is {valid_mountain} is a valid mountain: {is_valid_mountain(valid_mountain)}")
	print (f"Is {invalid_mountain} is a valid mountain: {is_valid_mountain(invalid_mountain)}")


if __name__ == "__main__":
	main()