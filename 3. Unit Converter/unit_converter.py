def help():
    print(""" Length: 
          meter (m)
          kilometer (m)
          Weight:
          kilograms (kg)
          pounds (lbs)
          Temperature:
          celcius (C)
          fahrenheit (F)""")

def length_converter(unit, number):
    unit_checker = unit.lower()
    if unit_checker == "kilometer":
        return number // 1000
    elif unit_checker == 'meter':
        return number * 1000

def weight_converter(unit, number):
    unit_checker = unit.lower()
    if unit_checker == "pounds":
        return number // 2.205
    elif unit_checker == 'kilograms':
        return number * 2.205
    
def temp_converter(unit, number):
    unit_checker = unit.lower()
    if unit_checker == "celcius":
        computation = (number * 9/5) + 32
        return computation
    elif unit_checker == 'fahrenheit':
        computation = (number - 32) * 5/9
        return computation
    
help()
mode = input('Mode of Conversion (Length, Weight, Temperature): ')



if mode.lower() == 'length':
    unit = input("Unit to be converted: ")
    number = int(input("Please put in a number "))
    converted = length_converter(unit, number)
    print(converted)
elif mode.lower() == 'weight':
    unit = input("Unit to be converted: ")
    number = int(input("Please put in a number "))
    converted = weight_converter(unit, number)
    print(converted)
elif mode.lower() == 'temperature':
    unit = input("Unit to be converted: ")
    number = int(input("Please put in a number "))
    converted = temp_converter(unit, number)
    print(converted)

