import csv
if __name__ == "__main__":

    with open("../csv/employees.csv", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    names = [f"{row[1]} {row[2]}" for row in rows[1:]]
    print ("All names:", names)
    
    names_with_e = [name for name in names if "e" in name.lower()]
    print("Names with 'e':", names_with_e)