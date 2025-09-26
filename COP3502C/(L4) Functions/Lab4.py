def fibonacci(n):
    i = 1
    first_num = 0
    second_num = 1
    while i < n:
        placeholder = first_num
        first_num = second_num
        second_num += placeholder
        i+=1
    return first_num

def is_prime(n):
    if n > 1:
        i = 2
        while i < n:
            if n % i == 0:
                return False
            else:
                i+=1
        return True
    else:
        return False

def print_prime_factors(n):
    print(f"{n} =", end=" ")
    i = 2
    first = True
    while i * i <= n:
        if n % i == 0:
            if not first:
                print(" * ", end="")
            print(i, end="")
            n //= i
            first = False
        else:
            i += 1
    if n > 1:
        if not first:
            print(" * ", end="")
        print(n)
    else:
        print()





