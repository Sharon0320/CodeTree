a,b = map(int,input().split())
numlist = [a,b]
start = 0
while (len(numlist) < 10):
    newnum = numlist[start] + numlist[start+1]
    if(newnum < 10):
        numlist.append(newnum)
    else:
        while(newnum >= 10):
            newnum = newnum % 10
        numlist.append(newnum)
    start += 1

for i in range(len(numlist)):
    print(numlist[i],end = " ")