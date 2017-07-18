def show(k):
    return k%10000000000

total=0;
for x in range(1,1000):
    t=1;
    for k in range (x):
        t=t*x
    total=total+t
print(show(total))