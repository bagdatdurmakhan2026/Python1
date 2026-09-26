import pandas as pd
employees = [
    {"name": "Arman", "age": 23, "salary": 140000},
    {"name": "Elena", "age": 34, "salary": 280000},
    {"name": "Timur", "age": 21, "salary": 90000},
    {"name": "Aigerim", "age": 29, "salary": 310000}
]
def find_r_employees(staff_list):
    r_emp=[]
    for emp in staff_list:
        if emp['salary']>150000:
            r_emp.append(emp['name'])
    return r_emp
print(find_r_employees(employees))
