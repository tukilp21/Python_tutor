# Python program to declare variables
# Basic datatype
# myNumber = 3
# print(type(myNumber))
  
# myNumber2 = 4.5
# print(type(myNumber2))
  
# myNumber ="helloworld"
# print(type(myNumber))

'''List'''
# Python program to illustrate a list 
# new_list = [4, 2, 7, 98, 123, 12]
# new_list.sort(reverse=True)
# print(new_list)

'''Tuple'''
# Python program to illustrate a tuple
my_tuple = ("hello", "world")

'''Indexing'''
new_list = [4, 2, 7, 98, 123, 12]

# Exercise: Print list in reverse order
# APPROACH 1
for idx in range(len(new_list)-1, -1, -1):
    print(new_list[idx])

print("--------------")
# APPROACH 2
new_list.reverse()

for idx in range( len(new_list) ):
    print(new_list[idx])