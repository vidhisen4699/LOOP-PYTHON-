'''23). Write a program to accept 10 numbers from the user and display the largest & smallest number'''
L = [ ]
i = 0
while(i<10):
    num = int(input("Enter number : "))
    L.append(num)
    i = i + 1
L.sort()
print("Largest number is : ", L[-1])
print("Smallest number is : ", L[0])