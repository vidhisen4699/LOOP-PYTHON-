'''Write a program to accept 10 numbers from the user and display it’s average''' 

s=0
i=0
while(i<10):
    num = int(input("Enter number : "))
    s = s + num
    i = i + 1
print("Average is : ", s/10)