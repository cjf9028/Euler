#1901년 1월 1일은 화요일부터 시작
#20세기 (1901년 1월 1일 ~ 2000년 12월 31일) 에서, 매월 1일이 일요일인 경우는 총 몇 번입니까?
year=1901
d=2
count=0
while(year<2001):
    for mon in range (1,13):
        if d == 0:
            count+=1
        if mon in (1,3,5,7,9,11):
            d=(d+3)%7
        elif mon in (2,6,8,10,12):
            d=(d+2)%7
        elif year%4==0:
            d=(d+1)%7
    year=year+1
print(count-1)