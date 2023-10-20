
import math

# '''
# This program is for PRINT
# '''
# ##########################################
def print_1():

    print("Hello World\nThis is Bill\nIm tutoring")
    print("~~~~~~~~~~~~~\n")

    print("Price\tTime\tName")
    print("100\t10\tBill")

##########################################
def print_2():
    # print default end is \n
    print("Hello", "sunny", "world", sep="__", end=" ")

'''
This is the print_number function

'''
##########################################
def print_number(first_number, second_number):
    # float, double
    a = first_number
    # int, unsigned int
    b = second_number

    c = a * b

    # print("The value of a is", a, "and b is", b, "and c is", c)
    # print("The value of a is {} and b is {} and c is {}".format(a, b, c))
    c = math.ceil(c)
    print(f"The value of a is {a} and b is {b} and c is the result of multiplication {c:.2f}")

    c = int(c)
    print(f"Convert the result to integer, this will round it up as well: {c}")
    print(f"The datatype of c is {type(c)}")


##########################################
# run as main file
if __name__ == "__main__":
    print("\n~~~~~~~~~~~~~")

    # print_1()
    # print_2()
    num1 = input("Enter the first number for the operation: ")
    num2 = input("Enter the second number for the operation: ")

    print_number(first_number = float(num1), second_number = float(num2))

    print("~~~~~~~~~~~~~\n")
