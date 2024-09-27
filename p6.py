#prime numbers

lower = int(input('Enter the number: '))
upper = int(input('Enter the number: '))

def prime(lower, upper):
    for i in range(lower, upper + 1):
        if i < 2: 
            continue
        is_prime = True 
        for j in range(2, i): 
            if i % j == 0: 
                is_prime = False
                break
        if is_prime:
            print(i)

prime(lower, upper)