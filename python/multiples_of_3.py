#Print from 1 to 20 and skip multiples of 3


for i in range(1, 21):
    if(i%3 == 0):
        continue
    print(i)