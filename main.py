import pandas as pd
import openpyxl

lesson = input("Please enter lesson name: ")


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


def addNewStudent(studentList):
    name = input("Name: ")
    surname = input("Surname: ")
    studentId = int(input("ID: "))
    points = int(input("Point: "))
    studentList.append(tuple((name, surname, studentId, points)))


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


def main():
    studentList = []
    exit = True
    while exit:
        print(
            "1. add a new student to list:\n"
            "2. remove a student from list\n"
            "3. edit a student from a list\n"
            "4. Create the excel file\n")
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
                print(df1)
                studentList = df1[['Name', 'Surname', 'ID', 'Points']].values.tolist()
        elif operand == 2:
            print('Removing will be added in a week')
        elif operand == 3:
            print('editing will be add in a week')
        elif operand == 4:
            finalTask(studentList)
            exit = False
        else:
            print('Invalid value , please enter a valid value !')


main()
