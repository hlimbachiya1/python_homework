import pandas as pd
import numpy as np
import json
import os

print("Running assignment4.py - latest version")

#task1
print("Task 1: Creating and manipulating DataFrames")
#1.1
print("\n1. Creating DataFrame from dictionary:")
data ={
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

#1.2
print("\n.2 Adding Salary column:")
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

# 1.3
print("\n3. Incrementing Age by 1:")
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print(task1_older)

#1.4
print("\n4. Saving to csv:")
task1_older.to_csv('employees.csv', index=False)
print("DataFrame saved to employees.csv")


#task2
print("\n Task 2: Loading data from csv to json")
#2.1
print("\n1. Reading csv file:")
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

#2.2
print("\n2. Creating and reading json file:")

json_data = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]

with open('additional_employees.json', 'w') as f:
    json.dump(json_data, f)
    
json_employees = pd.read_json('additional_employees.json')
print(json_employees)

#2.3
print("\n3. combining Dataframes:")
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)


#task3
print("\n task3: Data Inspection")
#3.1
print("\n1. First three rows:")
first_three = more_employees.head(3)
print(first_three)

#3.2
print("\n2. Last two rows:")
last_two = more_employees.tail(2)
print(last_two)

#3.3
print("\n3. dataFrame shape:")
employee_shape = more_employees.shape
print(f"Shape: {employee_shape}")

#3.4
print("\n4. dataFrame info:")
more_employees.info()

#task4
print("\n task4: data cleaning")

#4.1
print("\n1. Loading dirty data:")
dirty_data = pd.read_csv('dirty_data.csv')
print("original dirty data:")
print(dirty_data)

#4.2
print("\n2. creating copy for cleaning:")
clean_data = dirty_data.copy()

#4.3
print("\n3. removing duplicates:")
clean_data.drop_duplicates(inplace=True)
print("after removing duplicates:")
print(clean_data)

#4.4
print("\n4. converting age to numeric:")
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("after converting Age to numeric:")
print(clean_data)

#4.5 (this task is about replacing the known placeholders to numberics:)
print("\n5. Converting Salary to numeric:")
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print("After converting Salary to numeric:")
print(clean_data)

#4.6 (this task will fill missing values like the age with average or mean age, and salary with median of it)
print("\n6. filling missing values:")
age_mean = clean_data['Age'].mean()
salary_median = clean_data['Salary'].median()
clean_data['Age'] = clean_data['Age'].fillna(age_mean)
clean_data['Salary'] = clean_data['Salary'].fillna(salary_median)
print("After filling missing values:")
print(clean_data)

# 4.7  [Received help from mentor. Note: use regex only when the input string is really messy and need customized operation]
print("\n7. converting the hire-date to datetime:")
# clean_data['Hire Date'] = clean_data['Hire Date'].astype(str).str.strip() # todatetime = true ?
# clean_data['Hire Date'] = clean_data['Hire Date'].str.replace(r'\s+', '', regex=True)
# clean_data['Hire Date'] = clean_data['Hire Date'].str.replace(r'[^0-9/\-]', '', regex=True)
# clean_data['Hire Date'] = clean_data['Hire Date'].str.replace('/', '-')
# clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce', infer_datetime_format=True)
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], format='mixed')
print("After converting Hire Date:")
print(clean_data)


#4.8 (strip whitespace and camelcase the name and department)
print("\n8. Standardizing text data:")
clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print("After standardizing text:")
print(clean_data)



