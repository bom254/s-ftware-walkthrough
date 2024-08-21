# Using a list of tuples
people_list = [("Alice", 30), ("Bob", 25), ("Charles", 35)]

# Printing the names and ages from the list
print("Using List:")
for name, age in people_list:
	print(f"Name: {name}, Age: {age}")

# Using a dictionary
people_dict = {
	"Alice": 30,
	"Bob": 25,
	"Charles": 35
}

# Print names and ages from the dictionary
print("\nUsing Dictionary:")
for name, age in people_dict.items():
	print(f"Name: {name}, Age: {age}")
