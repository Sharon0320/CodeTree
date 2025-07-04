a,b = input().split()
la = len(a)
lb = len(b)
if (la > lb):
    print(a,la)
elif(la < lb):
    print(b,lb)
else:
    print("same")