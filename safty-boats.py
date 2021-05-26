### Number of boats required to save people

"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit.
 Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
 

Constraints:

1 <= people.length <= 5E104
1 <= people[i] <= limit <= 3E104
"""


def boats_to_save_people(list, limit):
	number_of_boats = 0
	left = 0
	right = len(list) - 1

	while (left < right):
		if left == right:
			number_of_boats += 1
			break
		elif left + right <= limit:
			number_of_boats += 1
			left += 1
			right -= 1
		else:
			number_of_boats += 1
			right -= 1
	return number_of_boats


def main():
	people = sorted([45,56,76,43,65,54,87,65,67,34,29,30])
	limit = 100
	print (f"No. of boats required to save {len(people)} people with weights {people} in Kg is: {boats_to_save_people(people, limit)}")


if __name__ == "__main__":
	main()