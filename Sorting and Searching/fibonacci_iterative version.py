#  Creating a fibnacci sequence using iterative menthod
def fibonacci(num):
    fibonacci_sequence=[0,1]
    for i in range(2,num+1):
        new_element=fibonacci_sequence[i-1]+fibonacci_sequence[i-2]
        fibonacci_sequence.append(new_element)
    return fibonacci_sequence
print(fibonacci(10))

#  Creating fibonacci sequence using recursive methon
def fibonacci_recursive(num):
    if 
