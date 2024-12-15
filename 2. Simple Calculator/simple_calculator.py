
def add(num_one, num_two):
    return num_one + num_two
def subtract(num_one, num_two):
    return num_one - num_two
def multiply(num_one, num_two):
    return num_one * num_two
def divide(num_one, num_two):
    return num_one / num_two

session = None

while not session:
    print("Arithmetic Operations are Add, Subtract, Multiply and Divide")
    operation = input("Please pick an operation: ")


    if operation.lower() == 'add':
        num_one = int(input("First Number: "))
        num_two = int(input("Second Number: "))
        result = add(num_one, num_two)
        print("The result is ", result)
        session = True

    elif operation.lower() == 'subtract':
        num_one = int(input("First Number: "))
        num_two = int(input("Second Number: "))
        result = subtract(num_one, num_two)
        print("The result is ", result)
        session = True

    elif operation.lower() == 'multiply':
        num_one = int(input("First Number: "))
        num_two = int(input("Second Number: "))
        result = multiply(num_one, num_two)
        print("The result is ", result)
        session = True

    elif operation.lower() == 'divide':
        num_one = int(input("First Number: "))
        num_two = int(input("Second Number: "))
        result = divide(num_one, num_two)
        print("The result is ", result)
        session = True

    else:
        print('Please answer with the proper choices')
