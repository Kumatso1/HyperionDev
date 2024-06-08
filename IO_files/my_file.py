my_file=open('my_file.txt','w')
my_file.write('This is my first file')
my_file=open('my_file.txt','r')
#print(my_file.read())
my_file=open('my_file.txt','a')
my_file.write('\nThis is my second line')
my_file=open('my_file.txt','r')
#print(my_file.read())
my_file.close()
my_file=open('my_file.txt','a')
my_file.write('\nThis text is added to to the second line')
my_file=open('my_file.txt','r')
#print(my_file.read())
lines=my_file.readlines()
print("".join(lines))
with open('my_file.txt', 'r+') as file:
    for line in file:
        print(line)
        print("The first 13 character of this line is: " + line[0:13])

contents = "" # Store the contents
with open('my_file.txt', 'r+') as file: # Open the file
    for line in file: # Iterate through the lines
        #file.write("This is another line")
        contents = contents + line # Add the contents of each line
       
    print(contents) # Print the content

    name=input("Enter your name: ")
    with open('output.txt','w') as file1:
        file1.write(name+"\n")
    file1.close()
    