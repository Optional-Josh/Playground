text_check = input("String to be checked if Palindrome: ")
text_clean = text_check.lower()

if text_clean == text_clean[::-1]:
    print(f'{text_clean} is a palindrome')
else: 
    print(f'{text_clean} is not a palindome')