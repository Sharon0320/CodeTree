one = []
one = "apple"
two = []
two = "banana"
three = []
three = "grape"
four = []
four = "blueberry"
five = []
five = "orange"

n = input()
arr = []

if (one[2] == n or one[3] == n):
    arr.append(one)
    print(one)
if (two[2] == n or two[3] == n):
    arr.append(two)
    print(two)
if (three[2] == n or three[3] == n):
    arr.append(three)
    print(three)
if (four[2] == n or four[3] == n):
    arr.append(four)
    print(four)
if (five[2] == n or five[3] == n):
    arr.append(five)
    print(five)
print(len(arr))