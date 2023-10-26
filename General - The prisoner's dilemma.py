#The prisoner's dilemma is when the two prisoners are given the option to either confess or stay silent. If one of them stays silent and the other one confesses, the confessor is released from prison and the silent one is in prison for 20 years. If they both stay silent they are both in prison for only 1 year each. If they both confess then they are both in prison for 5 years each. Design a program that simulates this with the user being prisoner A and the computer being prisoner B. It must have the computer choose different outcomes and the player should have the choice to play again.
import random

possibilities = ['stay silent', 'confess']
choice = input('Would you like to confess or stay silent? ')
outcome = possibilities[random.randint(0, 1)]

if choice == 'stay silent' and outcome == 'stay silent':
  print('Both of you stayed silent. You and the other prisoner have been sentenced to 1 year in prison')
elif choice == 'stay silent' and outcome == 'confess':
  print('You stayed silent, the other prisoner confessed. You have been sentenced to 20 years in prison and the other prisoner was released')
elif choice == 'confess' and outcome == 'stay silent':
  print('You confessed, the other prisoner stayed silent. The other prisoner has been sentenced to 20 years in prison and you were released')
else:
  print('Both of you confessed. You and the other prisoner have been sentenced to 5 years in prison')
