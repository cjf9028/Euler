num=5
total=0
while(num<=10000):
    sum=0
    sum1=0
    for x in range (1,int(num/2)+1):
        if(num%x==0):
            sum+=x
    for y in range (1,int(sum/2)+1):
        if (sum % y == 0):
            sum1 += y
    if sum1==num:
        total+=num
    num = num + 1
print(total)