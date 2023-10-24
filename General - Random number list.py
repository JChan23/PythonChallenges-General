#Use the random function to create a LIST (array) of 50 random numbers that you can use to calculate the Minimum, Maximum and mean average
import random

array = []
min = 101
max = -1
total = 0

for i in range(50):
  array.append(random.randint(0, 100))

print(array)

for i in range(50):
  if array[i] > max:
    max = array[i]
  if array[i] < min:
    min = array[i]
  total = total + array[i]

print('')
print('The smallest value in the array is', min)
print('The largest value in the array is', max)
print('The mean of the array is', total/50)
