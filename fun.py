def calculate_equation(a, b, c, x):
    result = (a * x**3) + (b * x**2) + c
    return result

# Taking input from the user
a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))
c = float(input("Enter the value of 'c': "))
x = float(input("Enter the value of 'x': "))

# Calculating the result of the equation
equation_result = calculate_equation(a, b, c, x)
print(f"The result of the equation {a}x^3 + {b}x^2 + {c} = 0 when x = {x} is: {equation_result}")
