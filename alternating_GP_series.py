#array
gp1=[]
r= int(input(''))
a=1
n = int(input())
b=1 
g= int(input('enter the ratio:'))
gp2=[]

for i in range(0, n):
    a = a*r 
    gp1.append(a)
for j in range (0,n):
    b=b*g
    gp2.append(b)

print(gp1)
count=1


for j in gp2:
    gp1.insert(count,j)        
    count+=2

res=[]
res[0]= 1
res[1]= 1
res.extend(gp1)
N = int(input("TERM"))
if N>1 :
    print (gp1[N])
else:
    print('Term not found')




