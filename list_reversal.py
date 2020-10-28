my_list = [1,2,3,4,5]
start = 0
end = len(my_list)-1
while start<end:
    # temp = my_list[start]
    my_list[start], my_list[end] = my_list[end], my_list[start]
    # my_list[start] = my_list[end] 
    # my_list[end] = temp
    start = start + 1
    end = end - 1
print(my_list)

