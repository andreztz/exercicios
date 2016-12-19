def is_prime(num):


    primo = True
    div = 2

    while div < num:
        if num % div == 0:
            primo = False
            break
        div += 1

    if primo and num > 1:
        return True
    else:
        return False


def n_primos(n):
    primes = []
    while n:
        if is_prime(n):
            primes.append(n)
        n -= 1
    return len(primes)


print(n_primos(10))
