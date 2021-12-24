def prime(n):
    f = 0
    if n == 1 or n == 0:
        f = 1
    for i in range(2, n):
        if n % i == 0:
            f = 1
    if f == 1:
        return 'n'
    else:
        return 'y'
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
if num1 > num2:
    for i in range(num2, num1 + 1):
        r = prime(i)
        if r == 'y':
            print(i)
else:
    for i in range(num1, num2 + 1):
        r = prime(i)
        if r == 'y':
            print(i)