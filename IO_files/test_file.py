""" This python program will iterate at each line of DOB text file and
it will also iterate each character in each line.
If the the character is found before any number or digit in the line 
then those characters are stored in the current_key variable. 
All the characters from any number are stored in the current_value string variable. 
After iterating the entire line, then the current_key is assigned as a key of the dictionary named dict_nb. 
Lastly, using for loop again all names are printed in their order using dict_nb.keys method and
 all Birthdates are printed using dict_nb. values() method. """

data = open("DOB.txt", "r") # Read the entire file content

dict_nb={} # Creating an empty dictionary
is_number = False
for line in data: #A for loop iterates through each line in the data string
  
    current_key = ""    #Stores the characters encountered before a number.
    current_value = ""  #Stores the characters encountered after a number.
    for char in line: # A for loop iterates through each character (char) in the line string
        if char.isdigit()==False  and is_number==False: # If character is not a digit and it is not a number.
            current_key += char   # adding the character to the current_key string.
        else:
            is_number=True # if character is a number
            current_value += char # adding the rest of characters from that number to current_value string.
    is_number=False
    
    # Assigning each 
    dict_nb[current_key]=current_value
 

# print(mp)
print("Name")
for keys in dict_nb.keys():
    print(keys)
print("\n"*2)
print("Birthdate")
""" When printing Birthdates, there will be a space between 
line because when the dictionary is being created from the file
there is inbuilt '\n' at the end of each value of dictionary. 
This causes the program to jump one line before printing new value."""
for values in dict_nb.values():
    print(values)
