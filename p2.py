def sqrt(n):
    approx = 0.5 * n
    better = 0.5 * (approx + n / approx)

    while better != approx :
        approx = better
        better =  0.5 * (approx + n / approx)
        
    return approx


n = int(input('Enter the number: '))

print(f'Sqrt of the num is {sqrt(n)}')