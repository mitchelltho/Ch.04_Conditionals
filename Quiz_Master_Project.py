'''
QUIZ MASTER PROJECT  (4pts)
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

correct = 0
questions = 0
answer = int(input("What is 8 * 8?: "))
if answer == 64:
    correct += 1
    questions += 1
    print("\033[1;32;49m Correct")
else:
    questions += 1
    print("\033[1;31;49m Incorrect")
    print("\033[1;31;49m The answer is: 64")

answer = input("What was the name of the first Star Wars BOOK: ").upper()
if answer == "Star Wars: From The Adventures of Luke Skywalker".upper() or answer == \
        "From The Adventures of Luke Skywalker".upper() or answer == "The Adventures of Luke Skywalker".upper():
    correct += 1
    questions += 1
    print("\033[1;32;49m Correct, it was: Star Wars: From The Adventures of Luke Skywalker, Released in November 1976")
else:
    questions += 1
    print("\033[1;31;49m Incorrect")
    print("\033[1;31;49m The answer is: Star Wars: From The Adventures of Luke Skywalker, Released in November 1976")

answer = input()