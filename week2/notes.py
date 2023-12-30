def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
user_input=int(input('enter number'))
result=is_prime(user_input)
if result:
    print(f"{user_input}is prime:true")
else:
    print(f"{user_input}is prime:false")