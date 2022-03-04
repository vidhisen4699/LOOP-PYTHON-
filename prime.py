# Write a program to check whether a number is prime or not.

num=int(input("Enter a number to check a prime number is this or not"))
count=0
i=num
while i>=1:
        if num%i==0:
                count=count+1
        i=i-1
if count==2:    
        print("prime")
else:
        print("Not Prime")    
        