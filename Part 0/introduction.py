# How you use the library
import math

A = 10
B = 4

# Compute square root of this A^4 = sqrt(10^4) = 100

equation = 1

# Do this 4 time
for i in range(B):
    equation = equation * A

final_equation = int(math.sqrt(equation))

print(final_equation)
print(type(final_equation))


