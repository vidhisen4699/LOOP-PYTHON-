# You have to print multiples of 3 from 1 to 40. While writing the code keep in mind that
#  the counter starts from 891?

i = 891
while i < 931:
    z = i - 890
    if z % 3 == 0:
        print(z)
    i = i + 1