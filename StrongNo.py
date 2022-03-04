# Python Program to find Strong Number using while loop
  
Num = int(input(" Please Enter any Number: "))
Sum = 0
Temp = Num
 
while Temp > 0:
    Factorial = 1
    Reminder = Temp % 10
    i=1
    while i <= Reminder:
        Factorial = Factorial * i
        i = i + 1
 
    print("\n Factorial of",Reminder, Factorial)
    Sum = Sum + Factorial
    Temp = Temp // 10
 
print("\n Sum of Factorials of a Given Number",Num, Sum)     
if (Sum == Num):
    print(" is a Strong Number",Num)
else:
    print(" is not a Strong Number",Num)
