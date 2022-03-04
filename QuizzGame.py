#This game ask multiple choice question about Canada. The game will also keep track of the score and it is going to print it at the end.

import time

#Welcome the user
print()
print("Welcome to the Simple Quiz Game!")
time.sleep(1)

#Chances
chances = 1
print("You will have", chances, "chance to answer correctly. \nPlease put the alphabet of the answer\n")
time.sleep(2)

#Score
score = 0

#question number 1
question_1 = print("1) What is the output for 'python ' [-3]?\n(a) 'o'\n(b) 't'\n(c) 'h'\n(d) Negative Index Zerro\n\n ")
answer_1 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_1, "\n\n")

time.sleep(2)

#question number 2
question_2 = print("2) Which is invalid in python for z = 5 ?\n(a)z=z++ \n(b) z=++z\n(c) z+=1\n(d) z-=1\n\n ")
answer_2 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_2):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_2, "\n\n")

time.sleep(2)

#question number 3
question_3 = print("3)Name the error that doesn’t cause program to stop/end, but the output is not the desired result or is incorrect.?\n(a) Syntax Error\n(b) RunTime Error\n(c) Logical Error\n(d) All of the Above\n ")
answer_3 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_3, "\n\n")

time.sleep(2)

#question number 4
question_4 = print("4) Suppose we have a set a = {10,9,8,7}, and we execute a.remove(14) what will happen ?\n(a) We can not the remove an element from the set \n(b) Method is executed but no exception is raised\n(c)Key Error is raised \n(d) There dosen't exit such method is remove\n\n ")
answer_4 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_4, "\n\n")

time.sleep(2)

#question number 5
question_5 = print("5) Which options are correct to create an empty set in Python?\n(a) {}\n(b) []\n(c) ()\n(d)set() \n\n ")
answer_5 = "d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_5, "\n\n")

time.sleep(1)

#print the score
while score >= 4:
    print("Well done! Your score was", score)
    break

while score <= 3:
    print("Better luck next time! Your score was", score)
    break
#Goodbye message
print("Thank you for playing the Simple Quiz Game!")