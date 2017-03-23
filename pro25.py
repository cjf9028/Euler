# 피보나치 수열중 첫번째 1000자리가 되는 수
order=1
k=2
num=2
while order<1000:
    order=order+num+1
    k=k+num*5+4
    num=num+1
print(k)
print(order)
a=order%1000
a=a/5
print(k-a*5)

#list=[1,1]
#for x in range (0,100):
#    lis=[int(list[x])+int(list[x+1])]
#    list=list+lis
#    print(list[x+2])
#6 5 5 4 5 5 5 4 5 5 5 5 4