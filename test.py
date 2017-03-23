# one two three four five six seven eight nine hundred thousand and
number=[0,3,3,5,4,4,3,5,5,4]
total=0
i=0
for x  in range (10):
    total=total+number[x]
for x in range (90):
    k=x+10
    y=k/10
    y=int(y)
    total=total+number[y]+number[y%10]+3
for x in range (900):
    k = x + 10
    y = k / 100
    y = int(y)
    z=(k%100)/10
    z=int(z)
    total = total + number[y]+number[z] + number[z % 10] + 7+3
total=total+8

print(total)


