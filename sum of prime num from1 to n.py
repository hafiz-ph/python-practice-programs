def sum_of_primes(n):
    
    total = 0 # To store the sum of primes
 # For loop from 2 to n (1 is not prime)
    for i in range(2, n + 1):
         is_prime = True
         j = 2
 # While loop to check if i is prime
         while j < i:
            if i % j == 0:
                 is_prime = False
                 break
            j += 1
         if is_prime:
            total += i
    return total
# Example
n = int(input("Enter a number: "))
print("Sum of primes from 1 to", n, "is:", sum_of_primes(n))
