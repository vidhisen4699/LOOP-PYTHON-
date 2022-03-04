# i=int(input("Enter number"))
# rev=0
# x=i
# while(i>0):
#     rev=(rev*10)+i%10
#     i=i//10
# if(x==rev):
#     print("Palindrom number")
# else:
#     print("Not a palindrom number")












i=int(input("Enter"))
rev=0
x=i
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
if(rev==x):
    print("palindrom")
else:
    print("Not Palindrom")        
