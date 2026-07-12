
Project: Student Record Management System



Problem Statement
A school wants a simple system to manage student records using Python.
Your task is to develop a Student Record Management System that allows users to store and manage student information using file handling.
The program should continuously display a menu and allow the user to perform different operations until the user chooses to exit.

Requirements
Your program must provide the following options:
1. Add Student
2. View All Students
3. Search Student
4. Exit

Functionalities
1. Add Student
When the user selects this option:
Ask the user to enter: 
Student Name 
Roll Number 
Marks 
Save the student information in a file named: 
students.txt
Each student record should be stored in the following format: 
Ali,101,88
Sara,102,91

2. View All Students
When the user selects this option:
Read all student records from the file 
Display each student record clearly on the screen 
Example Output
Name: Ali | Roll No: 101 | Marks: 88
Name: Sara | Roll No: 102 | Marks: 91

3. Search Student
When the user selects this option:
Ask the user to enter a student name 
Search for that student in the file 
If the student exists, display the complete record 
Otherwise display: 
Student not found

4. Exit
When the user selects this option:
Display a goodbye message 
Terminate the program 



Additional Instructions:
Use loops to repeatedly display the menu until the user exits. 
Use conditional statements to handle menu choices. 
Use proper file handling techniques for reading and writing data. 
Handle invalid menu options properly. 


Display grade according to marks: 
80+ → A 
70–79 → B 
60–69 → C 
Below 60 → Fail 
Display total number of student records stored in the file. 
Add an option to clear all records from the file. 



