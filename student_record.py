from dashboard import *

db={}

def list_of_student():
    print('-'*50)
    
    for name in db:
        
        print(f"Student Name: {db[name]['name']}")
        print(f"Student Marks: {db[name]['marks']}")
        print(f"Student Roll_no: {db[name]['roll_no']}")

        print('-'*50)

def add_new_student():

    uname    =input('Enter Student Name:')
    umarks   =input('Enter Student Marks:')
    uroll_no =input('Enter Student Roll_no:')

    name={}

    name['name']=uname
    name['marks']=umarks
    name['roll_no']=uroll_no

    db[uname] = name

    print(f'student {uname} added successfully ')

def update_student():
    uname=input('Enter student Name to updated: ')

    db[uname]['name'] =input('Enter update student name  ')
    db[uname]['marks'] =input('Enter update student marks ')
    db[uname]['roll_no'] =input('Enter update student roll_no')

    print(f'Student {uname} is updated successfully')

def search_student():
    name=input('Enter student Name to search: ')
    
    for name in db:
        
        print(f"Student Name: {db[name]['name']}")
        print(f"Student Marks: {db[name]['marks']}")
        print(f"Student Roll_no: {db[name]['roll_no']}")

def delete_student():
    name=input('Enter student Name to Delete: ')

    del db[name]

    print(f' student {name} is deleted successfully')

    
while True:

    ch=input('Enter Your Choice:')

    if ch == '1':
        list_of_student()
    
    elif ch== '2':
        add_new_student()

    elif ch== '3':
        update_student()

    elif ch== '4':
        delete_student()

    elif ch== '5':
        search_student()

    elif ch== '6':
        print('Exit From System')
        break
    else:
        print('Enter Valid Choice:')
        
    print('-'*50)
    
    choice = input("If you want to continue please enter:[yes/no]")
    if choice=='yes':
        dashboard()
    else:
        break

