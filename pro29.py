# 2 ≤ a ≤ 100 이고 2 ≤ b ≤ 100인 a, b를 가지고 만들 수 있는 a의 b 제곱은 중복을 제외하면 모두 몇 개입니까?
list=[]
count=0
for x in range (2,101):
    for y in range(2,100):
        num = x
        for z in range (y):
            num=num*x
            if num not in list and num != x:
                k=[num]
                list=list+k
                count+=1
print(count)

