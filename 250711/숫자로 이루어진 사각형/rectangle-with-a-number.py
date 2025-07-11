n = int(input())

# Please write your code here.
num_list = [1,2,3,4,5,6,7,8,9]

def machine(n,num_list):
    for i in range(n):
        for j in range(n):
            if (len(num_list) == 0):
                num_list = [1,2,3,4,5,6,7,8,9]
            print(num_list[0],end=" ")
            num_list.pop(0)
        print()

machine(n,num_list)