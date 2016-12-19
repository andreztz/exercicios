def fizzbuzz(num):
    if num % 3 == 0 and not num % 5 == 0:
        return 'Fizz'
    if num % 5 == 0 and not num % 3 == 0:
        return 'Buzz'
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    if num % 3 != 0 and num % 5 != 0:
        return num
