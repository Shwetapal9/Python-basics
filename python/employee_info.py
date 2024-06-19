n = int(input('Enter the number of Employees: '))
employees = {}
for i in range(n):
    name = input('Enter the name of Employee: ')
    salary = input('Enter the salary of Employee: ')
    employees[name] = salary

while True:
    print("Displaying Employee Details")
    name = input('Enter Employee name: ')
    salary = employees.get(name, -1)
    if salary == -1:
        print("Employee doesn't Exist")
    else:
        print('The salary of ',name, 'is',salary)
    choice = input('Do you want to know the salary of other employee? [yes| No] :')
    if choice == 'No':
        break
