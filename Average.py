''' 11 लोगों के वजन का इनपुट लें और फिर उनके औसत प्रिंट करें और फिर जांचें कि औसत वजन 5 का मल्टीपल है या नहीं?
 इसका मतलब यह है कि जब आप औसत वजन को 5 से विभाजित करेंगे, तो शेष 11 लोगों के वजन का इनपुट होना चाहिए
  और फिर उनके औसत प्रिंट करें और फिर जांचें कि औसत वजन 5 में से एक बहु है या नहीं?
 इसका मतलब यह है कि जब आप औसत वजन को 5 से विभाजित करेंगे, तो शेष 0 होना चाहिए। '''

'''Take input of weights of 11 people and then print their average and then check whether the average 
    weight is a multiple of 5 or not?
  This means that when you will divide the average weight by 5, the remainder should be 0.'''

# i=1
# average=0
# while(i<=11):
#     people=float(input("Enter the weight of the people"))
#     people=people+i
#     if people%11==0:
#         print("Average of the people",average)
#     i=i+1



i=0
sum=0
while i<=10:
  sum=int(input("Enter the weight of the people"))
  sum=i+sum
  #print(sum)
  i=i+1
average=sum/11
if average%5==0:
    print("weight is divisible by 5")
else:
  print("weight is not divisible by 5")  
      
print("Sum of the people age",sum)          
print("Average of the total age",average)    

# i=0
# s=0
# while i<=10:
#     num=int(input("Enter Number"))
#     s=num+s
#     i=i+1
#     print(s)

