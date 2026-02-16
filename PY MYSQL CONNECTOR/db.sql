CREATE DATABASE student;
USE student;

CREATE TABLE student_details (
    roll_number INT PRIMARY KEY,
    name VARCHAR(100),
    branch VARCHAR(50)
);
ALTER TABLE student_details
ADD address VARCHAR(255);

DESCRIBE student_details;

INSERT INTO student_details (roll_number, name, branch, address) VALUES
(1, 'Ravi', 'CSE', 'Delhi'),
(2, 'Anita', 'ECE', 'Bhopal'),
(3, 'Rahul', 'ME', 'Mumbai'),
(4, 'Pooja', 'CSE', 'Indore'),
(5, 'Aman', 'ECE', 'Patna'),
(6, 'Suman', 'IT', 'Delhi'),
(7, 'Neha', 'ME', 'Jaipur'),
(8, 'Rohit', 'CIVIL', 'Pune'),
(9, 'Kiran', 'CSE', 'Hyderabad'),
(10, 'Anjali', 'IT', 'Chennai');

DESCRIBE student_details;
SELECT * FROM student_details;


