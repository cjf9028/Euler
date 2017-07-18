def check(x):
    for k in range (2,x):
        if (x%k==0):
            return 0
    return 1
def check2(x,add):
    list=[]
    t=x
    while t>0:
        list.append(t%10)
        t=int(t/10);
    t=x+add
    list2=list.copy()
    while t > 0:
        if(t%10 not in list2):
            return 0;
        k = t % 10
        list2.remove(k)
        t = int(t / 10);
    t = x + add+add
    list2 = list.copy()

    while t > 0:
        if (t % 10 not in list2):
            return 0;
        k = t % 10
        list2.remove(k)
        t = int(t / 10);
    return 1;
def makeresult(x,add):
   result=x*100000000+(x+add)*10000+x+add+add
   print(result)

x=1001

while x<8000:
    if(check(x)==1):
        for add in range(1000,4500):
            if (check(x+add)==1 and x+add<10000):
                if(check(x+add+add)==1 and x+add+add<10000):
                    if(check2(x,add)==1):
                        makeresult(x,add)
    x=x+2
