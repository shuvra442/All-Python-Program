def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

start, end = map(int, input("Enter the range (start end): ").split())

prime_numbers = [num for num in range(start, end + 1) if is_prime(num)]
non_prime_numbers = [num for num in range(start, end + 1) if not is_prime(num)]

print("Prime numbers within the range:", prime_numbers)
print("Non-prime numbers within the range:", non_prime_numbers)
