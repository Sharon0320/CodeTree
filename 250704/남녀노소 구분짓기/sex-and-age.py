sex = int(input())
age = int(input())

if(sex == 0 and age >= 19):
    print("MAN")
elif(sex == 1 and age >= 19):
    print("WOMAN")
elif(sex == 0 and age < 19 and age > 0):
    print("BOY")
elif(sex == 1 and age < 19 and age > 0):
    print("GIRL")
else:
    print("NAN")