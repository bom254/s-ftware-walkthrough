# List of number
numbers = [1,2,3,4,5,6,7,8,9,10]
index = 0

# Using while loop to print even numbers
print("Even numbers using while loop:")
while index < len(numbers):
	if numbers[index] % 2 == 0:
		print(numbers[index])
	index += 1
