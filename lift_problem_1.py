N=int(input())  # max number in lift 
W=int(input()) # max weight of lift 
num=int(input()) # people waiting out
li=list(map(int,input().split())) # list of waiting people
li.sort()
x=0
cnt=0
for i in li:
  if(x>=W):
    break
  x+=i
  cnt+=1
print(cnt)
