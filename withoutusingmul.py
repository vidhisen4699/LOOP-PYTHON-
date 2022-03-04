'''num1=int(input('Enter 1 number'))
num2=int(input('Enter 2 number'))
i=1
sum=0
while i<num1:
    sum=sum+num2
    i=i+1
print(sum)    
'''

#How to print product of two numbers without using "*" operator in Python
num1=int(input("Enter a number for num1: "))#get input from user for num1
num2=int(input("Enter a number for num2: "))#get input from user for num2
product=0
for i in range (1,num2+1):  #Python for loop
 product=product+num1       #product+=num1
print("Multiplication of numbers: ",product) #Display multiplication of numbers
