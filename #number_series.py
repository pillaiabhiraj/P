#number_series
sev=[]
n= int(input(""))
for i in range (0,n):
    i = i*7
    sev.append(i)

six=[]
for j in range (0,n):
    j = j*6
    six.append(j)

N= int(input('TERM'))

count=1

for j in six:
    sev.insert(count,j)
    count+=2

if N <= n*2  :
    print(sev[N])
else:
    print('not found')