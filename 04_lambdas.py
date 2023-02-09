### Lambdas ###

sum = lambda  num1, num2: num1 + num2
print(sum(3, 9))

mult = lambda  num1, num2: num1 * num2 - 3
print(mult(3, 9))

def sum_three_values(value):
    return lambda num1, num2: num1 + num2 + value

print(sum_three_values(3)(5, 2))