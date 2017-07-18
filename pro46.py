import math

def check(n):
    for x in range(2,n-1):
        if(n%x==0):
            return 0;
    return 1;

def fincheck(x):
    for k in range(3,x):
        if(check(k)==1):
            num=(x-k)/2
            if(math.sqrt(num)%1==0):
                return 0;
    return 1;

for x in range (1,100000):
    k=x*2+1
    if(fincheck(k)==1 and check(k)==0):
        print(k)
        exit()



