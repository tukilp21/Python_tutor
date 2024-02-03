'''
Three common methods:
- Break
- Continue
- Pass

'''

# Break
##################################
# for i in range(10):
#     print(i)

#     # end at 7
#     if i == 7:
#         break

# --------------------
# s = "python is fun"
# # add "very" into the sentence

# ADD_STR = "very"
# search_idx = 0


# # loop go through each character
# for idx, char in enumerate(s):
#     # debug
#     # print(idx)
#     # print(char)

#     # break when it reaches the space after "s" in is
#     # get its index
#     if char == "s":
#         search_idx = idx
#         break

# # add the string
# new_s = s[:search_idx+1] + " " + ADD_STR + s[search_idx+1 : ]
# print(f"New string: {new_s}")


# Continue
##################################
# print even number only

# for i in range(10):
#     # if i % 2 == 0:
#     #     # only prnit if it even
#     #     print(i, end=", ")

#     if i % 2 != 0:
#         continue
#     print(i, end=", ")

# ----------------
# print the given list of number, except the RED list
    
import random
START = 0
END = 20

given_list = range(START, END)

#Generate 10 random numbers between the given list
red_list = random.sample(range(START, END), 5)
print(red_list)

for num in given_list:
    if num in red_list:
        continue

    # only print if it not in the RED list
    print(num, end=", ")

# Pass
##################################
class Animal:
    pass

class Dog(Animal):
    pass

# step1: for loop to go through the list
for i in range(list):
    pass

# step 2
print("hello")

# step 3
print("bye")






