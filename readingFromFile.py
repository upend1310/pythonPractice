# read mode
employee_file = open("employees.txt", "r")
print(employee_file.readable())
print(employee_file.readline())
print(employee_file.readlines())
print("////////////////////")
print(employee_file.read())
employee_file.close()

# append mode
employee_file = open("employees.txt", "a")
employee_file.write("\nToby - Human Resources")
employee_file.close()

# write mode
employee_file = open("employees.txt", "w")
employee_file.write("Toby - Human Resources")
employee_file.close()

# read and write
employee_file = open("employees.txt", "r+")
employee_file.write("Toby - Human Resources")
employee_file.close()
