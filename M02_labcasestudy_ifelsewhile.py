# Program Author: Cole Brzezinski
# Program Name: Honor Roll or Dean List Verifier
# Program Purpose: To gather information on a student and assess whether they've made honor roll or the deans list

last_name = input("Enter a student's last name (or 'ZZZ' to quit): ")

while last_name != "ZZZ":
    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List with a GPA of", gpa)
    elif gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll with a GPA of", gpa)
    else:
        print(first_name, last_name, "does not qualify for the Dean's List or Honor Roll with a GPA of", gpa)

    last_name = input("Enter a student's last name (or 'ZZZ' to quit): ")
