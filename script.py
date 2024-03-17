# Hamza Alsarakbi
# 101221018
# COMP 3005 Assignment 3 Question 1 script
import psycopg2, re, tabulate
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
headers = ['ID', 'FIRST NAME', 'LAST NAME', 'EMAIL', 'ENROLLMENT DATE']

# selects all students, prints them to console and returns them
def getAllStudents():
  # select all students to print to console
  cursor.execute('select * from students')
  rows = cursor.fetchall()
  
  # print
  print(tabulate.tabulate(rows, headers=headers, tablefmt='fancy_grid'))
  
  # return
  return rows


# adds a student to the students table 
def addStudent(first_name: str, last_name: str, email: str, enrollment_date: str):
  # add student
  cursor.execute(f"insert into students (first_name, last_name, email, enrollment_date) values ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')")
  # select added student
  print("Added record")
  cursor.execute(f"select * from students where first_name='{first_name}'")
  rows = cursor.fetchall()
  print(tabulate.tabulate(rows, headers=headers, tablefmt='fancy_grid'))
  

# updates a student's email by their student_id
def updateStudentEmail(student_id: int, new_email: str):
  # update student's email
  cursor.execute(f"update students set email = '{new_email}' where student_id={student_id}")
  
  # Print updated record
  print("Updated record")
  cursor.execute(f"select * from students where student_id='{student_id}'")
  rows = cursor.fetchall()
  print(tabulate.tabulate(rows, headers=headers, tablefmt='fancy_grid'))

# Deletes a student from the students table by the student_id
def deleteStudent(student_id: int):
  # for printing
  cursor.execute(f"select * from students where student_id={student_id}")
  rows = cursor.fetchall()
  
  # Delete student
  cursor.execute(f"delete from students where student_id={student_id}")
  
  # print deleted record
  print("Deleted record")
  print(tabulate.tabulate(rows, headers=headers, tablefmt='fancy_grid'))
  

# Gets a number within a range
def inputNumber(prompt: str, min: int, max: int) -> int:
  res = input(f'{prompt}\n$ ').strip()
  try:
    num = int(res)
  except ValueError:
    print('Invalid response, you must enter a number. Try again.')
  
    num = inputNumber(prompt, min, max)
  if num < min or num > max:
    print(f'You must enter a value between {min} and {max}. Try again.')
    num = inputNumber(prompt, min, max)
  return num

# Gets input for add student
def inputAddStudent()-> (str, str, str, str):
  first_name = input('Enter first name\n$ ').strip()
  last_name = input('Enter last name\n$ ').strip()
  email = inputStudentEmail()
  while True:
    enrollment_date = input('Enter entrollment date according to this format (YYYY-MM-DD)\n$ ').strip()
    if re.match(r'^\d{4}-\d{2}-\d{2}$', enrollment_date):
      break
    print('Invalid enrollment date format. Try again.')
  return first_name, last_name, email, enrollment_date
  
# Gets student email
def inputStudentEmail() -> str:
  while True:
    email = input('Enter email according to this format (email@domain.com)\n$ ').strip()
    if re.match(r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,}$', email):
      return email
    print('Invalid email format. Try again.')
  
def main():
  while True:
    print('[Main Menu]')
    print('\t1. Get all students')
    print('\t2. Add student')
    print('\t3. Update student email')
    print('\t4. Delete student')
    print('\t0. Exit')
    choice = inputNumber('Enter selection', 0, 4)
    
    if choice == 0:
      return
    elif choice == 1:
      getAllStudents()
    elif choice == 2:
      (first_name, last_name, email, enrollment_date) = inputAddStudent()
      addStudent(first_name=first_name, last_name=last_name, email=email, enrollment_date=enrollment_date)
    elif choice == 3:
      id = inputNumber('Enter student ID', 0, 9999)
      email = inputStudentEmail()
      updateStudentEmail(id, email)
    elif choice == 4:
      id = inputNumber('Enter student ID', 0, 9999999999999)
      deleteStudent(id)
      
  
main()

# closure
connection.close()