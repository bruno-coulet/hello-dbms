CREATE DATABASE SomeCompany;

USE SomeCompany;

CREATE TABLE Employees
(
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birthdate DATE,
    position VARCHAR(100),
    department_id INT
);

CREATE TABLE Departments
(
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100),
    department_head INT,
    location VARCHAR(100),
    FOREIGN KEY (department_id) REFERENCES Employees(department_id)
);

INSERT INTO Employees
    (employee_id, first_name, last_name, birthdate, position, department_id)
VALUES
    (1, 'John', 'Doe', '1990-05-15', 'Software Engineer', 1),
    (2, 'Jane', 'Smith', '1985-08-20', 'Project Manager', 2),
    (3, 'Mike', 'Johnson', '1992-03-10', 'Data Analyst', 1),
    (4, 'Emily', 'Brown', '1988-12-03', 'UX Designer', 1),
    (5, 'Alex', 'Williams', '1995-06-28', 'Software Developer', 1),
    (6, 'Sarah', 'Miller', '1987-09-18', 'HR Specialist', 3),
    (7, 'Ethan', 'Clark', '1991-02-14', 'Database Administrator', 1),
    (8, 'Olivia', 'Garcia', '1984-07-22', 'Marketing Manager', 2),
    (9, 'Emilia', 'Clark', '1986-01-12', 'HR Manager', 3);

INSERT INTO Departments
    (department_id, department_name, department_head, location)
VALUES
    (1, 'IT', 11, 'Headquarters'),
    (2, 'Project Management', 2, 'Branch Office West'),
    (3, 'Human Resources', 6, 'Branch Office East');



SELECT first_name , last_name , position
FROM employees;

UPDATE employees SET position = "Data Analyst" where employee_id = 2;

DELETE FROM Employees
WHERE employee_id = 9;

SELECT e.employee_id , e.first_name , e.last_name , d.department_name, d.department_head, d.location
FROM employees e
    join Departments d ON e.department_id = d.department_id;

SELECT e.employee_id , e.first_name , e.last_name , d.department_name, d.department_head, d.location
FROM employees e
    join Departments d ON e.department_id = d.department_id
where d.department_name = "IT";

SELECT e.employee_id , e.first_name , e.last_name , d.department_name, d.department_head, d.location
FROM employees e
    join Departments d ON e.department_id = d.department_id
where d.department_name = "Project Management";

SELECT e.employee_id , e.first_name , e.last_name , d.department_name, d.department_head, d.location
FROM employees e
    join Departments d ON e.department_id = d.department_id
where d.department_name = "Human Resources";

select d.department_name , e.last_name
from employees e
    join departments d on e.employee_id = department_head
order by department_name;


INSERT INTO Departments
    (department_id, department_name, department_head, location)
VALUES
    (4, 'Marketing', 8, 'Headquarters');

update employees set department_id = 4 where employee_id = 8
;

CREATE TABLE Project
(
    project_id INT PRIMARY KEY,
    project_name VARCHAR(255),
    start_date DATE,
    end_date DATE,
    department_id INT
);

INSERT INTO Project
    (project_id, project_name, start_date, end_date, department_id)
VALUES
    (1, 'IT Infrastructure Upgrade', '2024-01-01', '2024-12-31', 1),
    (2, 'Cloud Migration', '2024-03-01', '2024-09-30', 1),
    (3, 'Data Center Expansion', '2024-05-01', '2024-11-30', 1),
    (4, 'Cybersecurity Initiative', '2024-06-01', '2024-12-31', 1),
    (5, 'New Product Launch', '2024-02-01', '2024-07-31', 2),
    (6, 'Client Relationship Management', '2024-03-15', '2024-08-31', 2),
    (7, 'Employee Wellbeing Program', '2024-04-01', '2024-10-31', 3),
    (8, 'Recruitment Strategy Improvement', '2024-05-01', '2024-11-30', 3),
    (9, 'Digital Marketing Campaign', '2024-07-01', '2024-12-31', 4);

select
    d.department_name ,
    count(*) as task_num
from project p
    join departments d on p.department_id = d.department_id
group by d.department_name ;


