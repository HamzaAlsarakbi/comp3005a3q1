# Hamza Alsarakbi
# 101221018
# COMP 3005 Assignment 3 Question 1 script
import psycopg2;
# database parameters
params = {
  'host': 'localhost',
  'database': 'comp3005a3q1',
  'user': 'postgres',
  'password': 'postgres',
  'port': '5432'
}
# connection setup stuff
connection = psycopg2.connect(**params)
cursor = connection.cursor()


# selects all students, prints them to console and returns them
def getAllStudents():
  # select all students to print to console
  cursor.execute('select * from students')
  rows = cursor.fetchall()
  print(rows)
  return rows


# adds a student to the students table 
def addStudent(first_name: str, last_name: str, email: str, enrollment_date: str):
  # add student
  cursor.execute(f"insert into students (first_name, last_name, email, enrollment_date) values ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')")
  # select added student
  cursor.execute(f"select * from students where first_name='{first_name}'")
  rows = cursor.fetchall()
  print(rows)
  

# updates a student's email by their student_id
def updateStudentEmail(student_id: int, new_email: str):
  # update student's email
  cursor.execute(f"update students set email = '{new_email}' where student_id={student_id}")
  # select updated student
  cursor.execute(f"select * from students where student_id='{student_id}'")
  rows = cursor.fetchall()
  print(rows)

# Deletes a student from the students table by the student_id
def deleteStudent(student_id: int):
  # delete student
  cursor.execute(f"delete from students where student_id={student_id}")
  # select all students to print to console
  cursor.execute(f"select * from students")
  rows = cursor.fetchall()
  print(rows)

# Script stuff goes here
print("Get all students:")
getAllStudents()
print("\nAdd student:")
addStudent('Hamza', 'Alsarakbi', 'hamzaalsarakbi@cmail.carleton.ca', '2021-09-01')
print("\nUpdate student email:")
updateStudentEmail(4, 'ahmad@gmail.com')
print("\nDelete student:")
deleteStudent(4)


# closure
connection.close()