#guessing game in python
import random
 
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while random_number != guess:
        guess = int(input(f'guess a number between 1 and {x} '))
        if guess < random_number:
            print('sorry guess again. TOO low')
        elif guess > random_number:
            print('sorry guess again. Too high') 
    print(f"yeaah congrats. You have gussed the number  {random_number} corrrectly")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low #could also be high because low == high
        feedback = input(f'Is {guess} too high (H), Too low (L), or correct (C) ').lower()
        if feedback == 'h':
            high = guess -1 
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yeahh! The computer guessed your number, {guess}, correctly')

computer_guess(10)

