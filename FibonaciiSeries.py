# Make an algorithm that prints the first 100 numbers of the fibonacci series.

# Fibonacci series is shown here,
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# # Fibonacci series will start at 0 and travel upto below number
# Number = int(input("\nPlease Enter the Range Number: "))

# # Initializing First and Second Values of a Series
# First_Value = 0
# Second_Value = 1
           
# # Find & Displaying Fibonacci series
# for Num in range(0, Number):
#            if(Num <= 1):
#                       Next = Num
#            else:
#                       Next = First_Value + Second_Value
#                       First_Value = Second_Value
#                       Second_Value = Next
#            print(Next)


Number = int(input("\nPlease Enter the Range Number: "))

i=0
while i<Number:
    if i<=1:
        Next=i
    else:   
        Next=First_Value+Second_Value
        First_Value=Second_Value
        Second_Value=Next
        print(Next)
        i=i+1