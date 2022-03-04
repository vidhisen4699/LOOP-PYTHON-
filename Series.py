## 1/1! + 1/2! + 1/3! + …….. + 1/n!


num = int(input("Enter any number  : "))
sum = 0
fact = 1
i = 1
while(i < num):
      fact= fact*i
      sum= sum + i/fact
      i = i + 1
print("Sum is       :    ",round(sum, 2))