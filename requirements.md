# Database Schema

## Table

* Table name: `students`
* Fields:
  * `student_id`: `Integer`, `Primary Key`, `Auto-increment`
  * `first_name`: `Text`, `Not Null`
  * `last_name`: `Text`, `Not Null`
  * `email`: `Text`, `Not Null`, `Unique`
  * `enrollment_date`: `Date`

### Initial Data

```sql
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
```

## Application Functions

* `getAllStudents()`: Retrieves and displays all records from the students table.
* `addStudent(first_name, last_name, email, enrollment_date)`: Inserts a new student record into the students table.
* `updateStudentEmail(student_id, new_email)`: Updates the email address for a student with the specified student_id.
* `deleteStudent(student_id)`: Deletes the record of the student with the specified student_id.

## Instructions

1. Use the provided schema to create your students table in PostgreSQL.
2. Populate the table with the initial data provided above.
3. Develop an application that includes the functions listed.
4. Ensure your application can connect to the PostgreSQL database to call each of the functions and perform the operations.

### Documentation and Submission

* Your code must include comments explaining the purpose and functionality of each segment.
* Include a README file with:
  * Steps to compile and run your application.

#### Demonstration Video

1. Record a clear and concise video demonstrating:
   1. The database setup with the provided schema and data.
   2. The execution of each function in your application. For INSERT, UPDATE, and DELETE operations, demonstrate their effects in your database using pgAdmin.
2. Upload the video to a video-sharing service and ensure that the video is viewable through the link you provide.

## Submission Details

### GitHub Repository

1. Create a new public repository on GitHub for this assignment.
2. Commit the source code of your application, any database creation scripts, and your README file to this repository.
3. Ensure that your README file includes setup instructions and how to run your application.
4. The repository should be well-organized with a clear structure. For example, use separate directories for your database scripts and application code if needed.

### Video Demonstration

1. Record at most a 5 minutes video demonstrating the functionality of your application. Ensure that the video clearly shows the execution of each function and the corresponding effect on the database.
2. Upload the video to a video-sharing platform (like YouTube, Vimeo, etc.) or a cloud storage service that supports video sharing.
3. Add the link to your video in the README file of your GitHub repository.

### Submission via Bightspace

1. Submit the URL of your GitHub repository through Bightspace.
2. Include any additional remarks or comments in the submission notes if necessary.
