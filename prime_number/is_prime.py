user_input = int(input("Please enter an integer: "))


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False
    return True


if is_prime(user_input):
    print(f"'{user_input} is a prime number.")
else:
    print(f"'{user_input} is not a prime number.")
