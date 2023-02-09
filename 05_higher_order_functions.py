### Higher order functions ###
from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(num1, num2, f_sum):
    return f_sum(num1 + num2)

print(sum_two_values_and_add_value(3, 4, sum_one))
print(sum_two_values_and_add_value(3, 4, sum_five))

### Closures ###
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))

print(sum_ten(3)(9))

### Built-in Higher order functions ###
numbers = [2, 5, 10, 21]

#Map
def mult_two(number):
    return number * 2

print(list(map(mult_two,  numbers)))
print(list(map(lambda number: number * 2,  numbers)))

#Filter
def filter_even(number):
    if number % 2 == 0:
        return True
    return False

print(list(filter(filter_even, numbers)))
print(list(filter(lambda number: number % 2 != 0, numbers)))

#Reduce
def sum_two_values(num1, num2):
    return num1 + num2

print(reduce(sum_two_values, numbers))