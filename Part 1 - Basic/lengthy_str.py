
''' This program is for learning String datatype '''

str1 = "Hello World"
str2 = "Good morning"

# Concatenation
print(str1 + " " + str2 + " " + "this is amazing")
# Format string --> format any varible to str and print it
print(f"{str1} {str2} this is amazing")

# Indexing
##########################################
# Extract the 5th character in str1
# char_extract_idx = 4
# fifth_char = str1[char_extract_idx]
# print(f"The fifth character in {str1} is {fifth_char}")
# Get the last character 
str1_len = len(str1)
print(str1_len)
last_char = str1[str1_len - 1]
# print(f"The last character in {str1} is {last_char}")
# print(f"The last character in {str1} is {str1[-1]}")

# Slicing
print(f"The first word in str1", end=": ")
first_word = str1[:-3] # it excluding the last idex
print(f'{first_word}')

# Cool trick with indexing / slicing
# Reverse
print("\nReverse the str 1")
str1_rev = str1[::-1]
print(f"{str1_rev}")

# print(f"{reversed(str1)}")

# Replace a character
char_to_replace = '+'
str1_list = list(str1)
str1_list[5] = char_to_replace
print(str1_list)
str1 = ''.join(str1_list)
print(str1)
#  = char_to_replace
# print(str1)

# String method
txt = "welcome to the jungle"
x = txt.split()
print(x)
# Get the second word
print(x[1])

