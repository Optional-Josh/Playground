import random

correct_answer = random.randint(1,10)

user = int(input("Guess the right number (Numbers Only)"))

def answer_check(answer):
    if answer == correct_answer:
        print("You are correct!")
    else:
        print("You are incorrect!")

while True: 
    answer_check(user)
        

