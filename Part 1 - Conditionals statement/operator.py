
'''
Python operations
29 Oct
'''

######################################################
##########      Arithmetic Operators       ###########
######################################################

######################################################
def ellipse_equation(x, y, h, k, a, b):
    term_1 = ((x - h)**2) / (a**2)
    term_2 = ((y - k)**2) / (b**2)
    return term_1 + term_2

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
            
            elif operation == "div": # this always return as a float
                return num1 / num2
            
            elif operation == "divf": # division (floor) - "cut" away the floating points
                return num1 // num2

            elif operation == "mod":  # modulus - return the remainder
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
##########      Comparision Operators       ##########
######################################################
def check_even_odd(input_num):
    remainder = input_num % 2 
    # check
    if remainder == 0:
        # it is divisible by 2
        print("this number is EVEN")

    elif remainder == 1:
        print("this number is ODD")


def get_last_digit(input_num):
    return input_num % 10

def check_last_digit(last_digit):
    # check the digit if it equal to {0,2,4,6,8}
    if last_digit == 0 or last_digit == 2 or last_digit == 4 or last_digit == 6 or last_digit == 8:
        print("this number is EVEN")
    # elif last_digit == 2:
    #     print("this number is EVEN")
    # elif last_digit == 4:
    #     print("this number is EVEN")
    # elif last_digit == 6:
    #     print("this number is EVEN")
    # elif last_digit == 8:
    #     print("this number is EVEN")
    # remain cases
    else:
        print("this number is ODD")


######################################################
##########      Main code       ######################
######################################################
if __name__ == "__main__":
    print("=========================")

    # BIG NOTE HERE: Always try to specifise the input if you know the input type
    input_num = float(input("Enter your number to check whether it EVEN or ODD: "))

    last_digit = get_last_digit(input_num=input_num)
    check_last_digit(last_digit=last_digit)

    print("\nsecond method to check")
    check_even_odd(input_num= input_num)
    
    print("=========================")