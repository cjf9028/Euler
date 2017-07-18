list=[1]
lis=[]
total=0
def check(n):
    global list
    global total
    k=n
    sum=0
    while (1):
        sum=sum+list[int(k%10)]
        k=int(k/10)
        if(k<10):
            sum=sum+list[k]
            break
    if (n==sum):
        print(n)
        total+=n

for x in range (2,11):
    sum = 1
    for y in range (1,x):
        sum=sum*y
    list=list+[sum]
print(list)
for y in range (3,list[9]*7):
    check(y)

print(total)
