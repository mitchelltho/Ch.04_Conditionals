'''
QUIZ MASTER PROJECT  (4pts)
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

correct = 0
questions = 0
answer = input("What is 8 * 8?: ")
if answer == "64": #The input isnt casted to an int because it would cause an error if the user inputted something
    correct += 1   #that could not be converted to an int
    questions += 1
    print("\033[1;32;49m Correct")
else:
    questions += 1
    print("\033[1;31;49m Incorrect")
    print("\033[1;31;49m The answer is: 64")

answer = input("\033[1;38;49m What was the name of the first Star Wars BOOK: ").upper()
if answer == "Star Wars: From The Adventures of Luke Skywalker".upper() or answer == \
        "From The Adventures of Luke Skywalker".upper() or answer == "The Adventures of Luke Skywalker".upper():
    correct += 1
    questions += 1
    print("\033[1;32;49m Correct, it was: Star Wars: From The Adventures of Luke Skywalker, Released in November 1976")
else:
    questions += 1
    print("\033[1;31;49m Incorrect")
    print("\033[1;31;49m The answer is: Star Wars: From The Adventures of Luke Skywalker, Released in November 1976")

answer = input("\033[1;38;49m What was the real name of the baby yoda from The Mandalorian\nA. Greg \n"
               "B. Grogu \nC. George \n").upper()
if answer == "B" or answer == "GROGU":
    correct += 1
    questions += 1
    print("\033[1;32;49m Correct")
else:
    questions += 1
    print("\033[1;31;49m Incorrect")
    print("\033[1;31;49m The answer was B or Grogu")

answer = input("\033[1;38;49m How many movies are there in the star wars canon ")
if answer == "12":
    questions += 1
    correct += 1
    print("\033[1;32;49m Correct")
else:
    questions += 1
    print("\033[1;31;49m Incorrect")
    print("\033[1;31;49m The answer was 12")

answer = input("\033[1;38;49m How long was the original theater cut of star wars episode 4 in seconds ")
if answer.isdigit() and 7200 <= int(answer) <= 7920:
    questions += 1
    correct += 1
    print("\033[1;32;49m Correct")
else:
    questions += 1
    print("\033[1;31;49m Incorrect")
    print("\033[1;31;49m The answer was anywhere between 7200 and 7920 seconds")

answer = input("\033[1;38;49m Where is Jabba the Hutt's palace located ").upper()
if answer == str("TATOOINE").upper():
    questions += 1
    correct += 1
    print("\033[1;32;49m Correct")
else:
    questions += 1
    print("\033[1;31;49m Incorrect")
    print("\033[1;31;49m The answer was Tatooine")

answer = input("\033[1;38;49m Who built C-3PO\nA. Princess Leia\nB. Han Solo\nC. Anakin Skywalker \n").upper()
if answer == "C" or answer == "ANAKIN" or answer == "ANAKIN SKYWALKER":
    questions += 1
    correct += 1
    print("\033[1;32;49m Correct")
else:
    questions += 1
    print("\033[1;31;49m Incorrect")
    print("\033[1;31;49m The answer was Anakin Skywalker")

print("\033[1;32;49m Your score is: " + str(correct) + "/" + str(questions))
print("You got " + str((correct / questions) * 100) + "%")
totalgrade = (correct / questions) * 100
if totalgrade >= 90:
    print("Your grade is an A")
elif totalgrade >= 80:
    print("Your grade is a B")
elif totalgrade >= 70:
    print("Your grade is a C")
elif totalgrade >= 60:
    print("Your grade is a D")
else:
    print("Your grade is an F")
