list1 = [2, 3, 5, 4, 1]
list2 = [6, 4, 3, 2, 5]
new_list = []

for i in range(0, len(list1)):
    x = list1[i] * list2[i]
    new_list.append(x)
    
print(new_list)