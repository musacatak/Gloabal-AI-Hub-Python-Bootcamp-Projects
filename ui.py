import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=900
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        title=tk.Label(root)
        ft = tkFont.Font(family='Times',size=26)
        title["font"] = ft
        title["fg"] = "#333333"
        title["justify"] = "center"
        title["text"] = "Student Grade System"
        title.place(x=300,y=20,width=311,height=30)

        lessonEntry=tk.Entry(root)
        lessonEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        lessonEntry["font"] = ft
        lessonEntry["fg"] = "#333333"
        lessonEntry["justify"] = "left"
        lessonEntry["text"] = "Enter Lesson Name"
        lessonEntry.place(x=130,y=120,width=150,height=25)

        lessonLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        lessonLabel["font"] = ft
        lessonLabel["fg"] = "#333333"
        lessonLabel["justify"] = "center"
        lessonLabel["text"] = "Enter Lesson Name"
        lessonLabel["relief"] = "ridge"
        lessonLabel.place(x=130,y=95,width=150,height=25)

        confirmLesson=tk.Button(root)
        confirmLesson["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=12)
        confirmLesson["font"] = ft
        confirmLesson["fg"] = "#ffffff"
        confirmLesson["justify"] = "center"
        confirmLesson["text"] = "Confirm Lesson"
        confirmLesson.place(x=310,y=120,width=120,height=25)
        confirmLesson["command"] = self.confirmLesson_command

        subTitle=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        subTitle["font"] = ft
        subTitle["fg"] = "#333333"
        subTitle["justify"] = "center"
        subTitle["text"] = "LearnPython();"
        subTitle.place(x=340,y=60,width=195,height=30)

        addNewStudent=tk.Button(root)
        addNewStudent["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=12)
        addNewStudent["font"] = ft
        addNewStudent["fg"] = "#000000"
        addNewStudent["justify"] = "center"
        addNewStudent["text"] = "add a new student"
        addNewStudent.place(x=130,y=200,width=130,height=25)
        addNewStudent["command"] = self.addNewStudent_command

        removeStudent=tk.Button(root)
        removeStudent["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=12)
        removeStudent["font"] = ft
        removeStudent["fg"] = "#000000"
        removeStudent["justify"] = "center"
        removeStudent["text"] = "remove a student"
        removeStudent.place(x=130,y=240,width=130,height=25)
        removeStudent["command"] = self.removeStudent_command

        editStudent=tk.Button(root)
        editStudent["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=12)
        editStudent["font"] = ft
        editStudent["fg"] = "#000000"
        editStudent["justify"] = "center"
        editStudent["text"] = "edit a student"
        editStudent.place(x=130,y=280,width=130,height=25)
        editStudent["command"] = self.editStudent_command

        createExcel=tk.Button(root)
        createExcel["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=11)
        createExcel["font"] = ft
        createExcel["fg"] = "#000000"
        createExcel["justify"] = "center"
        createExcel["text"] = "Create the excel file"
        createExcel.place(x=130,y=320,width=130,height=25)
        createExcel["command"] = self.createExcel_command

        exit=tk.Button(root)
        exit["bg"] = "#ff0000"
        ft = tkFont.Font(family='Times',size=14)
        exit["font"] = ft
        exit["fg"] = "#ffffff"
        exit["justify"] = "center"
        exit["text"] = "Exit"
        exit.place(x=130,y=370,width=120,height=25)
        exit["command"] = self.exit_command

        pageTitle=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        pageTitle["font"] = ft
        pageTitle["fg"] = "#333333"
        pageTitle["justify"] = "center"
        pageTitle["text"] = "ADD A NEW STUDENT"
        pageTitle.place(x=450,y=160,width=134,height=30)

    def confirmLesson_command(self):
        print("command")


    def addNewStudent_command(self, pageTitle):
        pageTitle.config(text="ADD A NEW STUDENT")


    def removeStudent_command(self):
        pageTitle.config(text="Remove A STUDENT")


    def editStudent_command(self):
        print("command")


    def createExcel_command(self):
        print("command")


    def exit_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
