#Create a game where you guess a number from 1 to 100. The program should tell you if the number is higher or lower and check for non-valid input.
import random

number = random.randint(1, 100)
guess = -1
while guess != number:
  guess = int(input('Try to guess the number. It is between 1 and 100: '))
  if guess < 1 or guess > 100:
    print('Input numbers between 1 and 100')
    print('')
  elif guess > number:
    print('Number is smaller. Try again')
    print('')
  elif guess < number:
    print('Number is larger. Try again')
    print('')
print('Correct!')
