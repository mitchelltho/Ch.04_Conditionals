# 4.0 Jedi Training (40pts)  Name:___Thomas_____________
# Below each program list the mistakes found in comments.

# 1. Make the following program work. (3 mistakes)  (3pts)

midichlorians = float(input("Enter midichlorian count: "))
if midichlorians > 10000:
    print("You have serious Jedi potential")
else:
    print("Jedi, you will never be.")

# Bad indent?
# Mising colon
# Missing paren
# changed elif to else


# 2. Make the following program work. (3 mistakes)  (3pts)

x = int(input("Enter a number: "))
if x == 3:
    print("You entered 3")

#Fixed indent
#added cast to int
#changed = to ==
# added : to if statement

# 3. Make the following program work. (4 mistakes)  (4pts)

answer = input("What is the name of Poe Dameron's Droid? ")
if answer == "BB8":
    print("Correct!")
else:
    print("Incorrect! It is BB8.")

#Added : to if
#added : to else
#changed = to == in if
#Changed "a" to Answer

    # 4. Make the following program work. (4 mistakes) (4pts)

jedi = input("Name one of the top 3 greatest Jedi.")
if jedi == "Yoda" or jedi == "Luke Skywalker" or jedi == "Obi-Wan Kenobi":
    print("That is correct!")

#Changed x to jedi
#Added quote marks top if statement
#Fixed print line
#Fixed indent
#added jedi == to or

# 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
#    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.  (6pts)

print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?").upper()

if user_input == "A" or user_input == "JEDI MASTER":
    sensitivity = "1000"
elif user_input == "B" or user_input == "SITH LORD":
    sensitivity = "900"
elif user_input == "C" or user_input == "DROID":
    sensitivity = "0"
else:
    print("Not a choice")
    sensitivity = ""

print("Sensitivity: " + sensitivity)

'''
Added quotations in if statements comparing strings
Changed single = to == in if statements 
Changed "Else if" to elif
Added else statement for invalid selection
Made input not case sensitive 
'''

'''
6. NUMBER ANALYSIS PROGRAM  (10pts)
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero
3.) inclusively between -100 and +100

A small report will then be printed. Use the following to test your program:

In: 32  
Out:  Test 1: Even
      Test 2: Positive
      Test 3: Inclusive

In: -123  
Out:  Test 1: Odd
      Test 2: Negative
      Test 3: Exclusive
'''
num = int(input("What is your number"))
if num % 2 == 0:
    print("Test 1: Even")
else:
    print("Test 1: Odd")

if num < 0:
    print("Test 2: Negative")
elif num > 0:
    print("Test 2: Positive")
else:
    print("Test 2: 0")

if 100 >= num >= -100:
    print("Test 3: Inclusive")
else:
    print("Test 3: Exclusive")

'''
GRADING 2.0    (10pts)
-------------------
Copy your Grading 1.0 program below and then modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
semgrade = int(input("What is your semester grade "))
examgrade = int(input("What is your final exam grade "))
examworth = float(input("What was the final exam worth "))
semworth = 100.0 - examworth
weightedsem = semgrade * semworth
weightedexam = examgrade * examworth
totalgrade = (weightedexam + weightedsem) / 100.0
if totalgrade >= 90:
    print("Your grade is an A")
elif totalgrade >= 80:
    print("Your grade is a B")
elif totalgrade >= 70:
    print("Your grade is a C")
elif totalgrade >= 60:
    print("Your grade is a D")
else:
    print("Your grade is an F, Transfer to Jonhston!")