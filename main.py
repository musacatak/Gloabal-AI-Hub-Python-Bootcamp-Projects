import pandas as pd
import openpyxl

lesson_list = ['Math', 'Physics', 'Chemistry', 'Biology', 'Geography', 'History', 'English', 'Turkish']


def choose_lesson():
    i = 0
    for lessons in lesson_list:
        print(f"{i} - {lessons}")
        i += 1
    global lesson 
    choice = input(str("Choose a lesson: "))
    if choice == '0':
        lesson = lesson_list[0]
    elif choice == '1':
        lesson = lesson_list[1]
    elif choice == '2':
        lesson = lesson_list[2]
    elif choice == '3':
        lesson = lesson_list[3]
    elif choice == '4':
        lesson = lesson_list[4]
    elif choice == '5':
        lesson = lesson_list[5]
    elif choice == '6':
        lesson = lesson_list[6]
    elif choice == '7':
        lesson = lesson_list[7]
    else:
        print("Invalid value , please enter a valid value !")
        choose_lesson()
    
    



def gradeCalculator(points):
    if points >= 90 and points <= 100:
        return 'A'
    elif points >= 80 and points < 90:
        return 'B'
    elif points >= 70 and points < 80:
        return 'C'
    elif points >= 60 and points < 70:
        return 'D'
    elif points >= 50 and points < 60:
        return 'F'
    else:
        return 'FF'


def addNewStudent(studentList):
    name = str(input("Name: "))
    # validate name input
    while not name.isalpha():
        print("Invalid value , please enter a valid value !")
        name = str(input("Name: "))
        continue
    surname = str(input("Surname: "))
    # validate surname input with regex (only alphabetical characters)
    while not surname.isalpha():
        print("Invalid value , please enter a valid value !")
        surname = str(input("Surname: "))
        continue
    # girilen değer rakamlardan oluşmalı ve benzersiz olmalı(olmasa da olur).
    studentId = int(input("ID: "))
    
    # girilen değer 0-100 arasında olmalı ve rakamlar dışında karakter içermemeli
    points = int(input("Point: "))
    
    studentList.append(tuple((name, surname, studentId, points)))
    print("Student added successfully !\n")
    exitOrCont()

def removeStudent(studentList,id):
    for student in studentList:
        if(id == student[2]):
            studentList.remove(student)
    print("The student that ID is entered has removed successfully.")
    exitOrCont()


def finalTask(studentList):
    list = []
    for student in studentList:
        grade =gradeCalculator(student[3])
        succes = 'Fail'
        if grade != 'F':
            succes = 'Pass'
        list.append([student[2], grade, succes])

    indx = []
    for i in range(len(list)):
        indx.append(i+1)
    df = pd.DataFrame(list, index=indx, columns=['Student ID', 'Grade', 'Succes'])

    df.to_excel('studentGrades.xlsx', sheet_name=lesson + ' Grades')
    return list

def printStudentList(studentList):
    indx = []
    for i in range(len(studentList)):
        indx.append(i + 1)
    df = pd.DataFrame(studentList, index=indx, columns=['Name', 'Surname', 'Student ID', 'Points'])
    print(df)
    exitOrCont()
def printStudentGrades(studentGrade):
    indx = []
    for i in range(len(studentGrade)):
        indx.append(i + 1)
    df = pd.DataFrame(studentGrade, index=indx, columns=['Student ID', 'Grade', 'Succes'])
    print(df)
    exitOrCont()

def exitOrCont():
    inp = int(input('Chose a following operands:'
                    '1. continue\n'
                    '2. exit\n'))
    if inp == 2:
        exit()

def main():
    choose_lesson()
    studentList = []
    studentGrades = []
    exit = True
    while exit:
        print(
            "1. add a new student to list:\n"
            "2. remove a student from list\n"
            "3. edit a student from a list\n"
            "4. Create the excel file\n"
            "5. Print current student List\n"
            "6. Print current Student Grades\n"
            "7. Exit\n")
        operand = int(input("Please choose an operand: "))

        if operand == 1:
            type = int(input("how do you want to enter student info:\n"
                             "1. manual (type one by one\n"
                             "2. enter with .xlsx file that created before\n"))
            if type == 1:
                size = int(input('How many students you want to enter:'))
                for i in range(size):
                    addNewStudent(studentList)
            elif type == 2:
                df1 = pd.read_excel('studentsList.xlsx', sheet_name='Sayfa1')
                studentList = df1[['Name', 'Surname', 'ID', 'Points']].values.tolist()
                print("Student list is added successfully!")
                exitOrCont()
        elif operand == 2:
            if len(studentList) == 0:
                print('Please fill the studentList first. There are no any student to remove')
            else:
                rmStId = int(input('Enter student ID to remove: '))
                removeStudent(studentList, rmStId)
        elif operand == 3:
            print('Editing section will be add later!')
            exitOrCont()
        elif operand == 4:
            studentGrades = finalTask(studentList)
        elif operand == 5:
            if len(studentList) == 0:
                print('Please fill the studentList first. There are no any students to print')
            else:
                printStudentList(studentList)
        elif operand == 6:
            if len(studentGrades) == 0:
                print('Please fill the studentGrades first. There are no any data to print')
                exitOrCont()
            else:
                printStudentGrades(studentGrades)
        elif operand == 7:
            break
        else:
            print('Invalid value , please enter a valid value !')
            exitOrCont()


main()
