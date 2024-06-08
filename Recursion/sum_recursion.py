def adding_up_to(numbers, index):
    
    """ 
        Calculates the sum of all elements in a list up to a given index using recursion.

        arguments:
        numbers: A list of integers.
        index: The index point up to which the sum is calculated.

        Returns:
        The sum of all elements in the list up to the specified index. 
     """
    

    if index < 0 or index >= len(numbers):
        return 0  # Base case: invalid index returns 0

    return numbers[index] + adding_up_to(numbers, index - 1)  # Recursive call

def main():
    
    # Provides examples of using the adding_up_to function.
   
    print(adding_up_to([1, 6, 5, 8, 7,12, 13,16], 6))  # Output: 52
    print(adding_up_to([4, 3, 1, 5,9,11,6], 4))  # Output: 22


if __name__ == "__main__":
  main()
