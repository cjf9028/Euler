# 각 자리의 숫자를 5제곱 해서 더했을 때 자기 자신이 나오는 수와 그 합
result=0
for x in range(1000,999999):
    k=x
    sum=0
    while(1):
        y=int(k%10)
        y=y*y*y*y*y
        sum=sum+y
        k=int(k/10)
        if (k<10):
            sum=sum+k*k*k*k*k
            break
    if x==sum:
        result=result+x
        print(result)
print(result)