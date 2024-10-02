#calculate digits and alphabets

str = input('Enter the string: ')
d = 0
a = 0

for l in str:
    if l.isdigit():
        d += 1
    else: 
        a += 1
        
print('No of digits: ', d)
print('No of alphabets: ', a)
