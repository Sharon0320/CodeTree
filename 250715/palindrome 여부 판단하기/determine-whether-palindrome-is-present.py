A = input()

# Please write your code here.

arr = []
for i in A:
    arr.append(i)

new_arr = []

howlong = len(arr)
for j in range(howlong):
    new_arr.append(arr[howlong-1-j])

palindrome = 0

for z in range(howlong):
    if(new_arr[z] != arr[z]):
        palindrome += 1

if(palindrome == 0):
    print("Yes")
else:
    print("No")