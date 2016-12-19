
def maximo(a, b, c):
    major = a
    numbers = [a, b, c]
    for num in numbers:
        if major <= num:
            major = num
    return major
