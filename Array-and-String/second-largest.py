random = [3,6,7,1,2,9,5]

largest = random[0]
second_largest = random[0]

for i in random:

	if i > largest:
		second_largest = largest
		largest = i	
	elif i > second_largest:
		second_largest = i

print(second_largest)