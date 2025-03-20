# function implementation
# def function_name(parameters):
#     # Codes block
#     return results/values


# create a function with paramaters and return values
def add_numbers(a,b):
    return a + b

result = add_numbers(5,3) # usage cage

print("Sum: ", result) # displaying result to console


# Scope and variable life time (Global vs Local)

greeting = "Hi"

def say_hello():
    print(greeting + " from inside the function")

say_hello()
print(greeting + "from outside the function")


# modules and package (built in)
import math as m
print(m.sqrt(6))





