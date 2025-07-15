A = input()

# Please write your code here.

howlong = len(A)
arr = []

for i in A:
    arr.append(i)

new_set = set(arr)
if (len(new_set) >= 2):
    print("Yes")
else:
    print("No")