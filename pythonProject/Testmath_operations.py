# import math_operations
#
# result_add = math_operations.add(5,3)
# result_subtract = math_operations.substract(10,4)
# result_multiply = math_operations.multiply(2,6)
# result_divide = math_operations.divide(10,9)
#
# print("addition result:", result_add)
# print("subtract result:", result_subtract)
# print("multiply result:",result_multiply)
# print("division result:",result_divide)

### kisi module ke sare function call krne ke liye
from math_operations import *
result_add = add(5,3)
result_subtract = substract(10,4)
result_multiply = multiply(2,6)
result_divide = divide(8,2)
result_power = power(9,3)

print("result of add :",result_add)
print("result of sub :",result_subtract)
print("result of multiply :",result_multiply)
print("result of divide :",result_divide)
print("result of power :",result_power)