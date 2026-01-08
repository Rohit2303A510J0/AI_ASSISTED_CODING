# Write a Python program to print Fibonacci sequence up to n terms
# Take user input
# Do not use any user-defined functions

n = int(input("Enter the number of terms: "))

# Initialize first two terms
a, b = 0, 1

# Print the first term if n is greater than 0
if n > 0:
    print(a, end=" ")

# Print the second term if n is greater than 1
if n > 1:
    print(b, end=" ")

# Generate and print the remaining terms
for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

# Optimize this Fibonacci code
# Simplify variable usage
# Improve readability
n = int(input("Enter number of terms: "))

prev, curr = 0, 1

for _ in range(n):
    print(prev, end=" ")
    prev, curr = curr, prev + curr
print()

# Write a Python function to generate Fibonacci sequence up to n
# Use meaningful comments
def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Take user input
n = int(input("Enter the number of terms: "))
# Generate and print the Fibonacci sequence
fib_sequence = fibonacci_sequence(n)
print(*fib_sequence)


# Write an iterative Fibonacci program in Python
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = int(input("Enter number of terms: "))
fibonacci_iterative(n)

# Write a recursive Fibonacci program in Python
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq
    
n = int(input("Enter number of terms: "))
fib_sequence = fibonacci_recursive(n)
print(*fib_sequence)