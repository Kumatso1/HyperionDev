def largest_number(numbers):
    """
        Finds the largest number in a list of integers using recursion.
        arguments :
        numbers: A list of integers.

        Returns:
        The largest number in the list.
    """

    if len(numbers) == 1:
        return numbers[0]  # Base case: return the only element in a single-item list

        # Recursive call: compare the first element with the largest in the remaining list
    return max(numbers[0], largest_number(numbers[1:]))


def main():
    
    # Provides examples of using the largest_number function.
    
    print(largest_number([1, 4, 5, 3,8,11,7]))  # Output: 11
    print(largest_number([3, 10, 6, 8, 12, 4, 5,9]))  # Output: 12


if __name__ == "__main__":
  main()
