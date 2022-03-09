N=int(input())  # max number in lift 
W=int(input()) # max weight of lift 
num=int(input()) # people waiting out
li=list(map(int,input().split())) # list of waiting people
li.sort()
x=0
cnt=0
for i in li:
  if(x>=W or cnt>=N):
    break
  x+=i
  cnt+=1
print(cnt)
'''
10
680
15
67 54 33 59 60 72 48 23 56 10 14 32 40 20 80
'''
