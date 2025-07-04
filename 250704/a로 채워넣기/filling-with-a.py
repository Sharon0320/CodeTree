string = list(input())
num = len(string)
string_lists = string
string_lists[1] = 'a'
string_lists[num-2] = 'a'
print("".join(string_lists))