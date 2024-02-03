
# Enumerate
for idx, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
	print(idx, value)

print()
######################################################################
# Zip
names = ['Deep', 'Sachin', 'Simran']	 # list
ages = (24, 27, 25)		 # tuple

for name, age in zip(names, ages):
	print('Name: ', name)
	print('Age: ', age)


# Zip with dictionary
	
person_dict = {
    "Deep": 24,
	"Sachin": 27,
	"Simran": 25,
}
# still need to use zip to "let python know there are multiple lists"
for name, age in zip(person_dict.keys(), person_dict.values()):
	print('Name: ', name)
	print('Age: ', age)
	
print()
######################################################################

# python code to demonstrate working of sorted(), reversed()

# initializing list
list1 = [1, 3, 5, 6, 2, 1, 3]
list2 = ['c', 'k', 'a', 'w']

# using sorted() to print the list in sorted order
print("The list in sorted order is : ")
for num in reversed(list1):
	print(num, end=" ")

print("\r")

# # using sorted() and set() to print the list in sorted order
# # set and range are both a list of number
# # use of set() removes duplicates.
# print("The list in sorted order (without duplicates) is : ")
# for i in sorted(set(list1)):
# 	print(i, end=" ")


