"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

"""


def max_water_container(_list):
	maxarea = 0
	l = 0
	r = len(_list) - 1
	while (l < r):
		maxarea = max(maxarea, min(_list[l],_list[r])* (r-l))
		if _list[l] < _list[r]:
			l += 1
		else:
			r -= 1
	return maxarea


if __name__ == "__main__":
	heights = [5,4,3,6,7,8,3,2,4,5,7,8,9,7,6,3,3,3,3,3,4,5,3]
	print (heights)
	print (max_water_container(heights))