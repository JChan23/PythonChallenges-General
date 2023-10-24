#Ask for a number and the computer will tell you if you can divide it exactly by 3

num = int(input('Input a number: '))
if num % 3 == 0:
  print('Number is divisible by 3')
else:
  print('Number is not divisible by 3')
