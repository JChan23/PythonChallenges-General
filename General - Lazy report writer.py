#A lazy economics teacher wants to write his reports really quickly. Create a Random report writer with a list of generic comments. It should ask for the number of students and then generate a random comment for each student.	
import random

comments = [
    "Excellent performance in class.",
    "Consistently engaged and participates actively.",
    "Shows a strong understanding of the subject matter.",
    "Demonstrates good analytical skills.",
    "Needs to improve attendance and participation.",
    "Struggles with the course material and should seek help.",
    "Has the potential to excel with more effort.",
    "Could benefit from additional study and practice.",
    "Overall, a satisfactory performance in the course.",
]

number = int(input('How many students are there in the class? '))
for i in range(number):
  print(f"Student {i+1}: {comments[random.randint(0,8)]}")
