def get_mixed_list():
  """
  This function creates an empty list, prompts the user for elements,
  converts numbers to their appropriate type (int or float), and appends
  them to the list. It then returns the completed list.
  """
  my_list = []
  while True:
    element = input("Enter an element (or 'q' to quit): ")
    if element.lower() == 'q':
      break
    try:
      # Try converting to integer first
      my_list.append(int(element))
    except ValueError:
      try:
        # If conversion to int fails, try converting to float
        my_list.append(float(element))
      except ValueError:
        # If both conversions fail, assume it's a string
        my_list.append(element)
  return my_list

# Get the mixed list from the function
mixed_list = get_mixed_list()

# Print the final list
print("The mixed list is:", mixed_list)
print(str(mixed_list))
