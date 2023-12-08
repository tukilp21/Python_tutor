

'''

Main features of loops:
    - Looping - repeating codes
    - Ending condition


All type of loops:

    - while 
        * define the END conditions put in the bracket
        * if not, just while(1) and use break at where you want to END
    - for
        * (usually) go with "in" <--> for loop allow you to iterate through a "list"
'''


# NOTE: If you just want to use literally just LOOP FUNCTION - how many time the code is being repeated
num_loop = 5

# print(list(range(num_loop)))

# for item in range(num_loop):
#     print(f"This sentence will be print {num_loop} time")

#################################################################################
# NOTE: If the list has meaningful values - use can "reuse" it

shopping_list = ["meat", "apple", "banana", "mouse"]

# item_index = shopping_list.index("apple")
item_index = 1

for item in shopping_list:
    # print("hello: ")
    # Retur index of the specified item in the list
    print(f"{item_index}. {item}")
    item_index = item_index + 1

# 1. meat
# 2. apple
# 3. banana
# 4. mouse



