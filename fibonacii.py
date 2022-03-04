# 15. Write a program to print the Fibonacci series till n terms (Accept n from user


# n=int(input("Enter Number"))
# x=0
# y=1
# z=0
# while(z<=n):
#     print(z)
#     x=y
#     y=z
#     z=x+y

# patter................
# i=1
# while(i<=4):
#     j=1
#     while(j<=i):
#         print(i,end='')
#         j=j+1
#     print()    
#     i=i+1    

# prime....................

num=int(input("Enter Number"))
i=1
Counter=0
while(i<=num):
    if num%i==0:
        Counter=Counter+1
    i=i+1
if Counter==2:
    print("Prime Number") 
else:
    print("Not Prime Number")
               