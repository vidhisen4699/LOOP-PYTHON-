num=int(input("Enter Number"))
count=0
i=1
while(i<=num):
    if(num%i==0):
        count=count+1
    i=i+1
if(count==2):
    print("prime") 
else:
    print("Not prime")       
