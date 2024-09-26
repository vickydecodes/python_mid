def power(base, exp):
    if exp == 1:
        return base
    else:
        return base*power(base, exp-1)
    
    
base = int(input('Enter the number: '));
exp = int(input('Enter the number: '))

print(f'{power(base, exp)}')
    
    
