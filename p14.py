#selection sort

list = []
length = int(input('Enter the length: '))
for i in range(length):
    a = int(input('Enter the number to append: '))
    list.append(a)
    
print(list)

def selection_sort(list):
    for i in range(len(list)):
      smallest = i
      for j in range(i+1, len(list)):
        if list[j] < list[smallest]:
            smallest = j
            list[i], list[smallest] = list[smallest],list[i]
    return list

print(selection_sort(list))
   