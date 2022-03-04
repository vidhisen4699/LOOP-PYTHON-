# 14. Write a program to display the number names of the digits of if the number is 231 then output should be
# Two a number entered by user, for example Three One


num1 = input("Enter any number : ")
L1 = list(num1)
L = len(L1)
i=0
n = {0 : "Zero", 1 : "One", 2 : "Two", 3 : "Three", 4 : "Four", 5 : "Five", 6 : "Six", 7 : "Seven", 8 : "Eight", 9 : "Nine"}
while (i < L):
    print(n[int(L1[i])], end = " ")
    i = i + 1