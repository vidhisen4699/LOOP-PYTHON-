# Question: find the second number of the given user Number?


num=int(input("Enter Number"))
i=0
while(i<num):
    second_digit=(num//10)%10
    i=i+1
print(second_digit)







