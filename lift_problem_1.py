N,W=map(int,input().split())
num=int(input())
li=list(map(int,input().split()))
li.sort()
x=0
cnt=0
for i in li:
    x+=i
    cnt+=1
    if(x>=W or cnt>=N):
        break
print(cnt)

'''
10
680
15
67 54 33 59 60 72 48 23 56 10 14 32 40 20 80
10
'''
'''
6 120
10
23 45 18 22 10 14 67 30 24 8
6
'''
