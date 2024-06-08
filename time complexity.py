import matplotlib.pyplot as plt

# Function to calculate Fibonacci numbers
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        print(fib[i-1] + fib[i-2])
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Calculate the first 100 Fibonacci numbers
fib_sequence = fibonacci(20)
print(fib_sequence)
#Plot the Fibonacci numbers
plt.plot(range(1, 21), fib_sequence, marker='o', linestyle='-')
plt.title('First 100 Fibonacci Numbers')
plt.xlabel('Index')
plt.ylabel('Fibonacci Number')
plt.show()
