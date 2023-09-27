'''
QUIZ MASTER PROJECT  (4pts)
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

correct = 0
answer = int(input("What is 8 * 8?: "))
if answer == 64:
    correct =+ 1
    print("\033[1;32;49m Correct")
else:
    print("\033[1;31;49m Incorrect")
    print("\033[1;31;49m The answer is: 64")

answer = input("")