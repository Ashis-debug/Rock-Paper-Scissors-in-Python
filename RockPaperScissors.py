import random
def play():
    user = input("choose your move!! press 'r' for rock, 'p' for paper and 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])


    print(f' Your choice is {user} and the system\'s choice is {computer}')


    if user == computer:
        print('it\'s a tie\n')
        return 0
    if is_win(user,computer):
        print("you got a point!\n")
        return 1
    else:
        print("computer got a point\n")
        return -1

def is_win(player, opponent):
    #return when the player wins
    # r > s, s > p, p > r

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True 


n = int(input(('How many times you wanna pay the game: ')))
user_point = 0
computer_point = 0
for i in range(n):
    point = play()
    if point == 1:
        user_point = user_point + 1
        print(f'Your score : {user_point} and computer\'s score {computer_point}')
    elif point == -1:
        computer_point = computer_point +1
        print(f'Your score : {user_point} and computer\'s score {computer_point}')
    else:
        user_point = user_point + 0
        computer_point = computer_point + 0
        print(f'Your score : {user_point} and computer\'s score {computer_point}')

if user_point == computer_point:
    print('it\'s a tie')
elif user_point > computer_point:
    print("You won the game!!")
else:
    print("you lost the match!!")