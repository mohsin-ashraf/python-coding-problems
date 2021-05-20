# Move all the zeros in the list to the end in efficient ways

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-2^31 <= nums[i] <= 2^31 - 1
 

Follow up: Could you minimize the total number of operations done?
"""

def move_zeros(list):
	i = 0
	for number in list:
		if number != 0:
			list[i] = number
			i += 1
	for j in range(i,len(list)):
		list[j] = 0


def main():
	list = [1,2,0,5,0,2,0,5,4,7,0,9,0,7,8,0]
	print (list)
	move_zeros(list)
	print (list)

if __name__ == "__main__":
	main()
