#An evil maths teacher has locked his students in school until they manage to type the first 100 numbers of the Fibonacci sequence. Can you think of a quicker way to do it in Python?	
#term 1 is 1, not 0
fibonacci = [0, 1]
number1 = 0
number2 = 1
for i in range(99):
  num = fibonacci[i] + fibonacci[i+1]
  fibonacci.append(num)

print(fibonacci) 
