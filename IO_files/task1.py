def separate_names_birthdates(data_file):
  """
  Reads data from a text file, separates names and birthdates, and prints them
  in separate sections.

  Args:
      data_file (str): The path to the text file containing name-birthdate pairs.
  """

  try:
    with open(data_file, 'r') as file:
      lines = file.readlines()

    names = []
    birthdates = []
    for line in lines:
      # Handle potential empty lines or lines without the expected delimiter
      if line.strip():  # Check if line is not empty
        name, birthdate = line.strip().split(", ")
        names.append(name)
        birthdates.append(birthdate)

  except FileNotFoundError:
    print(f"Error: File '{data_file}' not found.")
  except ValueError:
    print(f"Error: Line in '{data_file}' does not contain the expected format 'name, birthdate'.")
  else:
    print("Name")
    for name in names:
      print(name)

    print("\nBirthdate")
    for birthdate in birthdates:
      print(birthdate)

# Assuming the data file is named 'DOB.txt' in the same directory
data_file = 'DOB.txt'
separate_names_birthdates(data_file)
