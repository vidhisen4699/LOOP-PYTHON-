# i=int(input("Enter any Number"))
# rev=0
# while(i>0):
#     rev=rev*10+i%10
#    # rev=rev//10
#     print(rev)
#     rev=rev//10
#     i=i+1


n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number: ",rev[0])
