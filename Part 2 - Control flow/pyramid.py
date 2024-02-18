''' EX 5

  *
 ***
*****

# Hint:
- print half pyramid (ignore the space)

*
***
*****
*******

0   1
1   3
2   5
3   7
n   2n+1

- add in the space
   *
  ***
 *****
*******

input = 4
relation line - space -input
0   3
1   2 = 4 - 1 - 1
2   1
3   0

     *
    ***
   *****
  *******
 *********
***********

input = 6
0   5
1   4
'''

'''
*
**
***
****
*****

relationship between LINE ORDER - NUM START PER LINE
'''

input_num = int(input("Enter a number: "))

# loop through lines
for line in range(input_num):
    
    # TODO: print the space before the star
    # method1 - using the range to iterate backward
    for num_space in range(input_num-line-1, 0, -1):
        print(" ", end="")

    # TODO: print star as a ODD half pyramid
    for num_star in range(line*2 + 1):
        print("*", end="")

    print("")




# # EX4

# # 1
# # 23
# # 456
# # 78910


# input_num = int(input("Enter a number: "))

# # start with 1
# num = 1

# # loop through lines
# for line in range(input_num):

#     # LOOP through certain number - depends on line number
#     for i in range(line+1):
#         print(num, end="")
#         num = num + 1

#     print("")

