from queue import Queue

students=Queue()

students.put('Dalison')
students.put('Alison')
students.put('Daliso')
students.put('Dalitso')

while not students.empty():
    current_student=students.get()
    print(current_student)