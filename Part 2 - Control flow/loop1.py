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
# num_loop = 5

# print(list(range(num_loop)))

# for item in range(num_loop):
#     print(f"This sentence will be print {num_loop} time")

'''
Display all the element (item) in a list
Format:
    
    # 1. meat
    # 2. apple
    # 3. banana
    # 4. mouse
'''
def print_list(target_list):
    for item in target_list:
        # print("hello: ")
        ''' Recommend method'''
        item_index = target_list.index(item) + 1  # Plus one because index of a list start at 0
        
        # Return index of the specified item in the list
        print(f"{item_index}. {item} - this is in the list {target_list}")

        '''This is a straightforward (manual) method'''
        # item_index = item_index + 1


def print_list_v2(target_list):
    for i in range(len(target_list)):
        item = target_list[i]
        item_idx = target_list.index(item) + 1
        print(f"{item_idx}. {item}")


def print_list_v3(target_list):
    for idx, item in enumerate(target_list):
        
        print(f"{idx + 1}. {item}")





