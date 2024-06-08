""" This python program creates a function named register_students which takes no parameters.
Within the function, the program asks the user to enter the number of students to be registered and 
this number is stored in a variable num_students and it is converted to integer.
It also open a file in append mode. It uses for loop to iterate over the number of students.
At evry iteration, it asks a user to enter ID and name of the student with that ID.
The student ID and student name is write to the file.
 """

def register_students():
  """
  Registers students for an exam venue and writes their IDs to a file.
  """
  num_students = int(input("Enter the number of students registering: "))
  with open("reg_form.txt", "a") as file:  # Open file in append mode
    for _ in range(num_students):
      student_id = input("Enter student ID: ")
      student_name=input("Enter the name of the student to be registered: ") # student name just added to the file more readable
      file.write(f"{student_id} : {student_name}\n----------\n")  # Write ID, name and separator


register_students()
print("Student registration complete!")
