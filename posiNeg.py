# Print this pattern using Loops.
# 1, -2, 3, -4, 5, -6 ..99, -100
# i * -1= -10
# i * -1= 2

i=0
while i<=100:
    if i%2==0:
        print(-i)
    else:
        print(i)
    i=i+1