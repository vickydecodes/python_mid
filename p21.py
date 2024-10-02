list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

print(list1)
print(list2)

for el in list2: 
    list1.append(el)
    
print(list1)

ind = int(input('Enter the index to delete: '))

del list1[ind]

print(list1)