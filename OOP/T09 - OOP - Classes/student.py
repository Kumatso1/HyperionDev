# Create  Student class
class Student():
    # Constructor method
    def __init__(self, age, name, gender, roll_number,grades, semester):
        self.age = age
        self.name = name
        self.gender = gender
        self.grades  = grades
        self.roll_number=roll_number
        self.semester=semester
   
    #  Method to calculate average grade
    def compute_average(self):
        average = sum(self.grades)/len(self.grades)
        #self.grades =grades
        print(f"The age of {self.name} is {self.age}")
        print(f"The average for {self.name} roll_number {self.roll_number} in the {self.semester}th semester is {average}")
       

# Create Student objects
philani  = Student(20, "Philani Sithole", "Male", 11211114, [64,65,76,83,57],5)
sarah = Student(19, "Sarah Jones", "Female", 1211113,[82,58,56,68,79],5)

# Method call
philani.compute_average()
sarah.compute_average()
#print(philani)

# Add in new objects and logic here, and above to test your understanding.
