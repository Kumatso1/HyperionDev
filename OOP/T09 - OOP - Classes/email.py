### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Creating the class, constructor and methods to create a new Email object.

# Declaring the class variable, with default value, for emails. 
 
# Initialising the instance variables for emails.

# Creating the method to change 'has_been_read' emails from False to True.

# --- Lists --- #
# Initialising an empty list to store the email objects.

# --- Functions --- #
# Building out the required functions for the program.
class Email:
    
    # Represents an email object with sender address, subject line, content, and read status.
   
    has_been_read = False  # Class variable, default: unread

    def __init__(self, email_address, subject_line, email_content):
        
        # Initializes an Email object.
       
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    
    def mark_as_read(self):
        
        # Marks the email as read and updates the has_been_read variable.
        
        self.has_been_read = True
        print(f"\nEmail from {self.email_address} marked as read.\n")

inbox = []  # Creating an empty list to store email objects
def populate_inbox():
    # populate_inbox creates three sample email objects and appends them to the inbox list. 
    # This is called during program startup.

    inbox.append(Email("info@hyperiondev.com", "Welcome to HyperionDev!",
                        "This is a welcome email..."))
    inbox.append(Email("bootcamp@hyperiondev.com", "Great work on the bootcamp!",
                        "Congratulations on completing the bootcamp..."))
    inbox.append(Email("noreply@exams.com", "Your excellent marks!",
                        "You achieved outstanding results in your exams...")) 

def list_emails():
    
    # Creating a function which prints the email’s subject_line, along with a corresponding number.
    if not inbox:
        print("\nYour inbox is empty.")
        return

    print("\nInbox:")
    for index, email in enumerate(inbox):
        print(f"{index}. {email.subject_line}")


def read_email():

    # The function read_email allows the user to select an email and displays its details, marking it as read.

    list_emails()
    if not inbox:
        return

    while True:
        try:
            index = int(input("\nEnter the index of the email to read (or -1 to exit): "))
            if index == -1:
                return
            elif 0 <= index < len(inbox):
                email = inbox[index]
                print(f"\nFrom: {email.email_address}")
                print(f"Subject: {email.subject_line}")
                print(f"\nContent:\n{email.email_content}")
                email.mark_as_read()
                break
            else:
                print("\nInvalid index. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

# --- Email Program --- #

# Calling the function to populate the Inbox for further use in your program.

# Filling in the logic for the various menu operations.

def main():
    """
    Main function to handle user interaction and program loop.
    """
    populate_inbox()

    while True:
        print("\nEmail Menu:")
        print("1. Read an email")
        print("2. View unread emails")
        print("3. Quit application")
        choice = input("\nEnter your choice (1-3): ")

        if choice == '1':
            read_email()
        elif choice == '2':
            unread_count = sum(not email.has_been_read for email in inbox)
            print(f"\nYou have {unread_count} unread emails.")
        elif choice == '3':
            print("\nQuitting application...")
            break
        else:
          print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
  main()