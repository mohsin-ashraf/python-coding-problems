# Find the maximum sum of K consective numbers in a list

def max_sum(list, window_size):
	if len(list) <= window_size:
		print ("Window size cannot be greater than or equal to the list size")
		return -1
	window_sum = sum([list[i] for i in range(window_size)])
	max_sum = window_sum
	
	for i in range(len(list) - window_size):
		window_sum = window_sum - list[i] + list[window_size + i]
		max_sum = max(max_sum, window_sum)
	return max_sum



def main():
	list = [12,41,45,23,1,3,76,1,23]
	print (max_sum(list,3))
	print (max_sum(list,2))
	print (max_sum(list,4))


if __name__ == "__main__":
	main()
