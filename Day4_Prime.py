num = int(input("Enter a positive number:"))
prime = 1
a = num // 2

if num < 0:
    print("Negative numbers are not allowed")
elif num == 0:
    print("Number entered by the user is 0")
else:
    for i in range(2, a + 1):
        is_prime = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime = i
    print("Greatest prime number is", prime)
