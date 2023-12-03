def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def check_neither_prime(num):
    return not is_prime(num)

number = 4
result = check_neither_prime(number)
print(f" Is {number} prime= {result}")   