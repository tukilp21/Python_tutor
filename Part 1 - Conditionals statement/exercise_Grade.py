
# -------------------------------------------------------------------------------------------
'''
# Exercise: Grade Calculator

# Write a program that takes input for a student's score and calculates their grade.
# The program should consider the following grading scale:
# - A: 90-100
# - B: 80-89
# - C: 70-79
# - D: 60-69
# - F: 0-59

# Your program should also perform input validation to ensure that the user
# If the user input wrong "things", the program should ask again (and again until it get the right input)
# enters a valid numerical score between 0 and 100.
'''
# -----------------------------------------------------------------------------------------------
print("########################################################")
A_range = list(range(90, 101))
B_range = list(range(80, 90))
C_range = list(range(70, 80))

# score = -1

# # Option 1: condition when the input is not a string? - to specific
# # Option 2: check the score variables? - check its value, check it type, ...
# # this is what we want: score in list(range(0, 101)) and isinstance(score, int)
# # --> by using NOT, you can flip the Condition (from a break conds to a continue conds)
# while (not(score in list(range(0, 101)) and isinstance(score, int))):
    
#     try: 
#         score = int(input("input your score: "))
#         # Validate the value
#         if not(score in list(range(0, 101)) and isinstance(score, int)):
#             print("Number is invalid - input again\n")
#         # Once it REALLY validated:
#         elif score in A_range:
#             print("You just scored an A")
#         elif score in B_range:
#             print("You just scored an B")
#         elif score in C_range:
#             print("You just scored an C")
       
#         # once it finished, the score should already be validated

#     except ValueError:
#         print("Value Error - input again\n")

        
ask_again_flag = 1 #true

# Option 1: condition when the input is not a string? - to specific
# Option 2: check the score variables? - check its value, check it type, ...
# this is what we want: score in list(range(0, 101)) and isinstance(score, int)
# --> by using NOT, you can flip the Condition (from a break conds to a continue conds)
while (ask_again_flag == 1):

    try:
        score = float(input("input your score: "))

        # Validate the value
        # if not (score in list(range(0, 101)) and isinstance(score, int)):
        if not( score >= 0 and score <= 100 and isinstance(score, float)):
            print("Number is invalid - input again\n")
            continue

        # Once it REALLY validated, start the conditional statement
        # elif score in A_range:
        elif score >= 90 and score <= 100:
            print("You just scored an A")
        # elif score in B_range:
        elif score >= 80 and score < 90:
            print("You just scored an B")
        # elif score in C_range:
        elif score >= 70 and score < 80:
            print("You just scored an C")
        else:
            # continue
            pass

        ask_again_flag = 0 #false
        # define condition to whether keep looping / stop

    except ValueError:
        print("Value Error - input again\n")


# math consideration
# [90, 100]
# [80, 90)