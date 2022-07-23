# PYBTCM2_learnPython
Group project for Global AI Hub Python Bootcamp.

## Group Members
| Name & Surname |
| ------------- |
|Ahmet Musa Çatak|
|Nesrin Yakar|
|Alperen Özdemir|
|Ahmet Çakmak|
|Adem Hatay|

### Project Description
Basic student grade system in Python.

#### Rules
* This system will be implemented by Python.
* Final project folders and files will upload to : https://forms.gle/t8WXBBfmWJSA2rzG6
* Deadline : 23 July 22

##### Tasks
* Choose a lesson for the system. (Math,Physic,Linear Algebra etc.)
* Set the point gaps. (Ex: 100-80 -> A , 80-60 -> B)
* Create a system that take inputs like name,surname,id,examPoints,pass/fail with these datas create a dataframe  and hold these datas in excel file.

###### Instructions
* First execute the 'main.py' file.
* When you execute to main ,you will access the choseLesson screen.(fig1)
  * ![Fig1](https://github.com/musacatak/Gloabal-AI-Hub-Python-Bootcamp-Projects/blob/main/Project%201/Figures/fig1.png?raw=true)
  * Enter number between 0-7 to select lesson.
* Then you will reach the main menu that contains adding,removing,editing students and show current sudent,grade list.
  * ![Fig2](https://github.com/musacatak/Gloabal-AI-Hub-Python-Bootcamp-Projects/blob/main/Project%201/Figures/fig2.png?raw=true)
  * Enter number between 1-7 to select desired operation.
* **Main Menu
  * '1. Add a new student to list' => section used for adding student to studentList
    * In this section you two option to add new student information.
    * First is manual entering that is required entering datas one by one from user.
    * Second is get student datas from studentList.xlsx file.
  * "2. Remove a student from list" => section used for removing student to studentList with studentID.
  * "3. Edit a student from a list" => section will be used for editing student datas in future.
  * "4. Create the excel file" => section used for extracting studentGrades to studentGrades.xlsx file.
  * "5. Print current student List" => section used for printing current students (in dataframe not excel file).
  * "6. Print current Student Grades" => section used for printing studentGrades that extracted to excel file befor.
  * "7. Exit" => Stop terminating the program.



