arr = [5,9,7]

def second_largest_number(arr):
	
	largest = 0
	second_largest = 0

	for i in arr:
		if i > largest:
			second_largest = largest
			largest = i
		elif i > second_largest and i != largest:
			second_largest = i

	
	print(second_largest)


second_largest_number(arr)