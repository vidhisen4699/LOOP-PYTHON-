# 9). Write a program to display all even numbers that fall between two numbers (exclusive both numbers)entered by the user.

num=int(input("Enter the number"))
i=1
while(i<=num):
    if(i%2==0):
        print("Even Number is",i)
    # else:
    #     print("Odd Number",i)    
    i=i+1

