def calculator(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
        print(f"the result of sum is {num1} + {num2} = {result}")
        return result
    
    elif operator == "-":
        result = num1 - num2
        print(f"the result of subtraction is {num1} - {num2} = {result}")
        return result
    
    elif operator == "*":
        result = num1 * num2
        print(f"the result of multiplication is {num1} * {num2} = {result}")
        return result
    
    elif operator == "/":
        result = num1 / num2
        print(f"the result of division is {num1} / {num2} = {result}")
        return result
    else:
        return "Invalid operator"


if __name__ == '__main__':
    print("Welcome to the calculator of python".center(50, "-"))
    value1 = float(input('input the first number: '))
    value2 = float(input('input the second number: '))
    operator = input('input operator (+, -, *, /): ')
    calculator(value1, value2, operator)
