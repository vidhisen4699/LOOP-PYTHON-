# Question 4
# Print this pattern using Loops.

# 1, -2, 3, -4, 5, -6 ..99, -100

i=0
while i<=10:
    num=int(input("Enter Number"))
    num1=num1*-i
    num2=num2*i
    i=i+1
    print(num1)
    print(num2)
