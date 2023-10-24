#Write a small program to check that input is a float and generate an error if it is not

num = float(input('Please enter a decimal number: '))
if num % 1 == 0:
  print('Error. Please enter a decimal number, not an integer.')
else:
  print('Number accepted.')
