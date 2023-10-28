
'''
Python operations
29 Oct
'''

######################################################
##########      Functions       ######################
######################################################

######################################################
def play_around_with_arithmetic():
    num1 = 64
    num2 = 6
    operation = input("Enter the operation: ")
    result = int(arithmetic(num1=num1, num2=num2, operation=operation))

    print(f"The result is {result}")
    print(f"The result dataype is {type(result)}")

######################################################   
# basic operator
# only do the math - because every function should be doing one thing

def arithmetic(num1=1, num2=1, operation="div"):
    # Validate the number
    # Both input number should be numbers - or in other words, float or int
    if isinstance(num1, float):
        # if the code is able to "GOES" in here
        # we know that num1 is an integer
        # so, let try validate the other number

        if isinstance(num2, float):
            # Yay, both numbers are numbers now (integer)

            if operation == "add":
                return num1 + num2
            
            elif operation == "sub":
                return num1 - num2
            
            elif operation == "mul":
                return num1 * num2
            
            elif operation == "div":
                return num1 / num2
            
            elif operation == "divf":
                return num1 // num2

            elif operation == "mod":
                return num1 % num2
            
            elif operation == "exp":
                return num1 ** num2
            
            else:
                return -1
        
        return -1
            
    return -1

''' COding note:
- usually, 0 represent "nothing" --> if a code return 0, it means that no errors appear
- usually, -1 represent "error" --> if a code return -1, it means that there is an error
'''


######################################################    
# Define all the paramters of a division
# In the form of A = B * C + D
def display_division(num1, num2):
    dividend = num1
    divisor = num2
    quotient = arithmetic(num1=dividend, num2=divisor, operation="divf")
    remainder = arithmetic(num1=dividend, num2=divisor, operation="mod")

    if quotient == -1 or remainder == -1:
        print("Something went wrong in the arithmetic function")
    
    else:
        print("")
        # print(f"{dividend} = {divisor} * {quotient} + {remainder}")
        print(f"{dividend} : {divisor} = {quotient}, and we remain {remainder}: .20f")


######################################################
##########      Main code       ######################
######################################################
if __name__ == "__main__":
    print("=========================")

    # BIG NOTE HERE: Always try to specifise the input if you know the input type
    num1 = float( input("Enter the first number for the operation: "))
    num2 = float( input("Enter the second number for the operation: "))

    display_division(num1, num2)
    
    print("=========================")