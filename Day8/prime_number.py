def checkPrime(n):
    if( n == 1 or n == 0 or n == -1):
        print(f"{n} is not a prime number.")
        return 0
    for i in range (2, round(abs(n)/2)+1):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            return 0
    print(f"{n} is a prime number.")

num = int(input("Enter a number: "))
checkPrime(num)
