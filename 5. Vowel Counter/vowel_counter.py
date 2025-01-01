vowels = ['a', 'e', 'i', 'o', 'u']

text_subject = input('Text which will be counted the amount of vowels it has: ')
text_check = text_subject.lower().strip()
counter = 0

for character in text_check:
    if character in vowels:
        counter += 1
if counter >= 1:
    print(f'{text_subject} has {counter} vowels')
else:
    print(f'{text_subject} has 0 vowels')
