#linear search


def linear_search(list):
    search= int(input('Enter the search element: '))
    flag = 0
    i = 0
    while i < len(list):
        if search == list[i]:
            flag = 1
            break
        i = i + 1
        
    if flag == 1:
        print(f'The item found at the index {i}')
    else:
        print('Item not found')






list = []

length = int(input('Enter the number: '))

for i in range(length):
    a = int(input('enter the value to append: '))
    list.append(a)
    
linear_search(list)
    
    

        
        
        