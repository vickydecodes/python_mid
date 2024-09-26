def computeGcd(x, y):
    if x > y:
        small = y
    else:
        small = x
    
    for i in range(1, small + 1):
        if x % i == 0 and y % i == 0:
            gcd = i
        
    return gcd


num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))

print(f'The gcd of the numbers is {computeGcd(num1, num2)}')