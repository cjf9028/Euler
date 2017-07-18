def check(k):
    list=[]
    while k>1000:
        list.append(k%10)
        k=int(k/10)
    num=len(list)
    while k>0:
        if(k%10!=list[num-1]):
            return 0
        k = int(k / 10)
        num=num-1
    return 1

def check2(k):
    for x in range (100,1000):
        if (k%x==0 and k/x>100 and k/x<1000):
            return 1
    return 0

for x in range (100000,1000000):
    if(check(x)==1):
        if (check2(x)==1):
            print(x)