'''Question: 1

Write a program that prints all those numbers from 1 to 100 which are divisible by 7.

The output should come as follows :-

7
14
21
28
35
42
49
56
63
70
77
84
91
98'''

i=0
while i<=100:
    if i%7==0:
        print(i)
    i=i+1
else:
    print("this number not divisible by 7")