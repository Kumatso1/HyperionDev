class Course:
    """
    Represents a course with a name, ID, and head office location.
    """
    head_office_location = "Cape Town"  # Class variable
    
    contact_website = "www.hyperiondev.com"

    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id

    def contact_details(self):
        """
        Prints the course contact details (head office location).
        """
        
        print(f"\nCourse Contact Details: ")
        print("Please contact us by visiting", self.contact_website)

        print(f"Head Office Location: {self.head_office_location}")

class OOPCourse(Course):
    """
    Represents an Object-Oriented Programming (OOP) course with additional details.
    """
    def __init__(self, name, course_id):
        super().__init__("OOP Fundamentals"course_id)  # Call parent constructor
        self.name = "Fundamentals of Computer Science"
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        """
        Prints the course description and trainer information.
        """
        print(f"\nCourse Details: {self.name}")
        print(f"Description: {self.description}")
        print(f"Trainer: {self.trainer}")

    def show_course_id(self):
        """
        Prints the course ID number.
        """
        print(f"\nCourse ID: #{self.course_id}")


def menu():
  """
  Creates an OOPCourse object and calls its methods.
  """
  course_1 = OOPCourse(12345)
  course_1.contact_details()
  course_1.trainer_details()
  course_1.show_course_id()


if __name__ == "__main__":
  menu()
