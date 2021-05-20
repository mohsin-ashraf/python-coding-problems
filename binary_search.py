

def binary_search(list, target):
	left = 0
	right = len(list)-1
	while left <= right:
		mid = (right + right) // 2
		if list[mid] == target:
			return mid
		elif list[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return -1

def main():
	list = [1,2,3,4,5,6,7,8,9,10,11]
	print (binary_search(list, 5))
	list.remove(5)
	print (binary_search(list,5))


if __name__ == "__main__":
	main()
