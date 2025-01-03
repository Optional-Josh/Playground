print('This program will check if the number you inserted is an odd or even number')
number_check = (input('Input a number: '))
number_convert = int(number_check)

if number_convert % 2 == 1:
    print('It is an odd number')
elif number_convert % 2 == 0: 
    print('It is an even number')