import sqlite3
import os

# Database file name
DB_NAME = "company.db"

# Remove any old database file so the example starts fresh.
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

# Connecting to SQLite
conn = sqlite3.connect(DB_NAME)

# Creating a cursor
cur = conn.cursor()

# Creating tables
cur.execute("CREATE TABLE department (id INTEGER PRIMARY KEY, name TEXT, location TEXT)")
cur.execute("CREATE TABLE employee (id INTEGER PRIMARY KEY, name TEXT, deptid INTEGER)")

# Inserting records into the department table
# Five realistic Indian city department records
department_records = [
    (1, "HR", "Chennai"),
    (2, "IT", "Bengaluru"),
    (3, "Finance", "Mumbai"),
    (4, "Sales", "Delhi"),
    (5, "Marketing", "Hyderabad")
]

# Inserting records into the employee table
# Employees include one valid department assignment, one missing department assignment, and departments with and without employees.
employee_records = [
    (1, "Aarav", 1),
    (2, "Priya", 2),
    (3, "Rahul", 99),
    (4, "Sneha", 2),
    (5, "Meera", 3)
]

# Executing SQL for department records
cur.executemany("INSERT INTO department (id, name, location) VALUES (?, ?, ?)", department_records)

# Executing SQL for employee records
cur.executemany("INSERT INTO employee (id, name, deptid) VALUES (?, ?, ?)", employee_records)

# Commit changes
conn.commit()

# Fetching all records from employee table
cur.execute("SELECT id, name, deptid FROM employee ORDER BY id")
employees = cur.fetchall()

# Fetching all records from department table
cur.execute("SELECT id, name, location FROM department ORDER BY id")
departments = cur.fetchall()

# Displaying employee records in a beginner-friendly format
print("Employees:")
print("ID | Name | DeptID")
print("------------------")
for emp_id, name, deptid in employees:
    print(f"{emp_id} | {name} | {deptid}")

print()

# Displaying department records in a beginner-friendly format
print("Departments:")
print("ID | Name | Location")
print("----------------------")
for dept_id, name, location in departments:
    print(f"{dept_id} | {name} | {location}")

# Query: show employee names who work in the HR department
cur.execute("""
    SELECT e.name
    FROM employee e
    JOIN department d ON e.deptid = d.id
    WHERE d.name = 'HR'
    ORDER BY e.name
""")
hr_employees = cur.fetchall()

print()
print("Employees in HR Department:")
print("Name")
print("----")
for (name,) in hr_employees:
    print(name)

# Closing the cursor and database connection
cur.close()
conn.close()
