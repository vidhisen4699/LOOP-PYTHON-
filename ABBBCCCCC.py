n=int(input("Enter Number of row"))
k=1
i=1
while(i<=n):
    j=1
    while(j<=k):
        print(chr(64+i),end="")
        j=j+1
    print()
    i+=1
    k=k+2

