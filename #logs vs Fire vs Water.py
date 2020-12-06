#logs vs Fire vs Water 
#Fire burns Logs, Logs make bridge over water, Water puts out fire

from random import randint
player = input ('Fire(f), Logs(l), Water(w)')

if player == 'f':
    print('fire')
elif player == 'l':
    print('log')
elif player == 'w':
    print('water')
else:
    print(' Nigga enter valid choice')

choosen = randint(1,3)
if choosen == 1:
    computer = 'f'
    print('fire')
elif choosen == 2:
    computer = 'l' 
    print('log')
else: 
    computer = 'w'
    print('water')

if player == computer:
    print('its a Draw')
elif player == 'f' and computer == 'l':
    print('Not every time u win. play again i dare u')
elif player == 'f' and computer == 'w':
    print('You lose BItch')
elif player == 'l' and computer == 'f':
    print('You lose BItch')
elif player == 'l' and computer == 'w':
    print('nice luck Bitch')
elif player == 'w' and computer == 'l':
    print('nice luck')
elif player == 'w' and computer == 'f':
    print('You lose BItch')
else:
    print('You a noob ??')
    