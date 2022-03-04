
i=int(input("Enter any Number"))
orig=i
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("Armstorm Number")
else:
    print("Not Armstorm Number")   


# num=int(input("Enter any Number"))
# sum=0
# temp=num
# while temp>0:
#     r=temp%10
#     sum=sum+r**3
#     temp=temp//10
# if sum==num:
#     print("Armstorm Number")
# else:
#     print("Not Armstorm Number")   
    