# 30). Write a program to find the sum of following series
# 1 + 8 + 27 …………n terms

# n=int(input("Enter Number"))
# i=1
# s=0
# while(i<n):
#     s=s+i**3
#     print("Sum of the Series",s)
#     i=i+1



n=int(input("Enter"))
s = 0
i = 1
while(i <= n):
   s = s + i ** 3
   i = i + 1
   print(s)

