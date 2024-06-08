class Adult:
    
    # Represents an adult with name, age, hair colour, and eye colour attributes.
    
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self):
        
        # Prints a message indicating the person's driving eligibility based on age.
        
        if self.age >= 18:
            print(f"\n{self.name} is old enough to drive.")
        else:
            print(f"\n{self.name} is too young to drive.")
    

class Child(Adult):
    
    # Represents a child inheriting attributes from Adult and overriding the can_drive() method.
   

    def can_drive(self):
    
        # Overrides the parent's can_drive() method to explicitly state the person is too young.
    
        print(f"\n{self.name} is a child and cannot drive yet.")


def main():
    
    # Prompts user for information and creates an Adult or Child object based on age.
    
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    hair_colour = input("Enter hair colour: ")
    eye_colour = input("Enter eye colour: ")

    if age >= 18:
        person = Adult(name, age, hair_colour, eye_colour)
    else:
        person = Child(name, age, hair_colour, eye_colour)

    person.can_drive()


if __name__ == "__main__":
  main()
