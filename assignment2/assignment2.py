import csv
import os
from datetime import datetime 

#task 2
def read_employees():
    employees_dict = {}
    rows_list = []
    
    try:
        
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            
            first_row=next(reader)
            employees_dict["fields"] = first_row
            
            for row in reader:
                rows_list.append(row)
                
            employees_dict["rows"] = rows_list
        
        return employees_dict
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]}, Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e)._name_}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    
employees = read_employees()
print("Employees loaded:", employees)

#task 3
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")
print("Employee ID column index:",employee_id_column)

#task 4
def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]

#task5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches

#task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

#task 7
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]

sorted_rows = sort_by_last_name()
print("employees sorted by last name")

#task8
def employee_dict(row):
    emp_dict ={}
    
    for i in range(len(employees["fields"])):
        field_name = employees["fields"][i]
        if field_name != "employee_id":
            emp_dict[field_name]= row[i]
            
    return emp_dict 

test_employee_dict = employee_dict(employees["rows"][0])
print("Sample employee dict:", test_employee_dict)

#task 9
def all_employees_dict():
    all_emp_dict ={}
    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        all_emp_dict[emp_id] = employee_dict(row)
    return all_emp_dict

all_emp_dict = all_employees_dict()
print("All employees dict created")

#task 10
def get_this_value():
    return os.getenv('THISVALUE')

#task 11
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
    
set_that_secret("my new secret")
print("Custom module secret:", custom_module.secret)

#task 12
def read_minutes():
    def read_minutes_file(filename):
        minutes_dict ={}
        rows_list = []
        
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                
                first_row = next(reader)
                minutes_dict["fields"]=first_row
                
                for row in reader:
                    rows_list.append(tuple(row))
                minutes_dict["rows"] = rows_list
            return minutes_dict
        
        except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")

    minutes1 = read_minutes_file('../csv/minutes1.csv')
    minutes2 = read_minutes_file('../csv/minutes2.csv')
    
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print("Minutes files loaded")

#task 13
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    combined_set=set1.union(set2)
    return combined_set

minutes_set = create_minutes_set()
print("Minutes set created with", len(minutes_set), "unique entires")

#task14
def create_minutes_list():
    minutes_list_temp = list(minutes_set)
    
    minutes_with_dates = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
        minutes_list_temp
    ))
    return minutes_with_dates

minutes_list = create_minutes_list()
print("Minutes list with datetime objects created")

#task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    
    sorted_with_strings = list(map(
        lambda x: (x[0], x[1].strftime("%B %d, %Y")),
        minutes_list
    ))
    
    try:
        with open('./minutes.csv','w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            for row in sorted_with_strings:
                writer.writerow(row)
        print("Sorted minutes written to minutes.csv")
        
    except Exception as e:
        trace_back = traceback.extract_tb(e._traceback_)
        stack_trace=list()
        for trace in trace_back:
            stack_trace.append(f'file: {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    return sorted_with_strings

final_sorted_list = write_sorted_list()
print("Assignment 2 is done!")