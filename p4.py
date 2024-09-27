#max number search


list = []

length = int(input('Enter the number'))

for i in range(length):
    a = int(input('enter the value to append: '))
    list.append(a)
    

maxno = list[0]

for i in range(len(list)):
    if maxno < list[i]:
        maxno = list[i]
        

print(maxno)