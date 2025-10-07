"""
1)add new employee
2)print all employees
3)delete by age
4)update salary by name
5)end the program

"""
def input_valid_int(msg, start=0, end=None):    #this is a utility(helping) function
    #keep iterating till the valid input is put
    #hidden assumption: both start and end either value or none, that is bad
    while True:
        inp = input()
        if not inp.isdecimal(): #checking if it is a number
            print('invalid input.')
        elif start != None and end != None:
            if int(inp) not in range(start, end+1):
                print('invalid range.')
            else:
                return int(inp)
        else:
            return int(inp)
        

class Employee:
    #holds data and basic functions for an employee
    def __init__(self, name, age, salary):
        self.name, self.age, self.salary = name, age, salary

    def __str__(self):
        return f'Employee: {self.name} has age {self.age} and salry: {self.salary}'

    def __repr__(self):
        return f'Employee(name={self.name}, age={self.age}, salary={self.salary})'
        

class Employees_Manager:
    # holds a list of employees and has implementations for menu options
    def __init__(self):
        self.employees = []    
    
    def add_employee(self, name, age, salary):

        self.employees.append(Employee(name, age, salary))

    def list_employees(self):
        if len(self.employees) == 0:
            print('No employees')
            return
        
        for emp in self.employees:
            print(emp)

    def delete_employees_with_age(self, age_from, age_to):
        #remove from the back
        for idx in range(len(self.employees)-1, -1, -1):
            emp = self.employees[idx]
            if age_from <= emp.age <= age_to:
                print('\tDeleting employee: ', emp.name)
                self.employees.pop(idx)
        #tip: pop from the middle of the list is slow O(n)!
        #one trick is to:
        #for every item to delete, swap it with the last
        #e.g. if we will delete 3 items, swap them to be the last 3 items in list
        #then delete them
        #pros: very efficient
        #cons: we altered the list order, it depends on the app.
        
        #another trick is to mark the removed person with none
        #and if their is a new employee just add him to one of the none
        #this way complete no deletion at all!
        #u can have anotherplaylist with none locations
        #cons: if there are many removed employees it itee=rates alot
        #and it will affect the list_employees function

        #solution: after somethershold, recreate a new fresh employees list

    def find_employee_by_name(self, name):

        for employee in self.employees:
            if employee.name == name:
                return employee
            return None

    def update_salary_by_name(self, name, salary):
        employee = self.find_employee_by_name(name)
        if employee == None:
            print('Employee not found')
        else:
            employee.salary = salary



class Frontend_Manager:     #backend
    #print the menu, get a choice and call the employee manager

    def __init__(self):
            self,employees_manager = Employees_Manager()

    def menu(self):
        message = [
        '1)add new employee',
        '2)print all employees',
        '3)delete by age',
        '4)update salary by name',
        '5)end the program'
        ]
        print('\n'.join(message))
        msg = f'Enter your choice from 1 to {len(message)}: ' 
        # writing the len(message) instead of 5 so it would be updated automatically if any item is added
        return input_valid_int(msg, 1, len(message))

    def run(self):
        while True: 
            choice = input('Enter your choice: ')

            if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
                print('Invalid Input...Try again')
                continue          
                    
                    
            if choice == '1':
                print('Enter employee data.\n')
                name = input('Enter employee name: ')
                age = input('Enter employee age: ')
                salary = input('Enter employee salary: ')
                Employees_Manager.add_employee()

            elif choice == '2':
                print('**Employees List**')
                Employees_Manager.list_employees()

            elif choice == '3':
                age_from = input_valid_int('Enter age from: ')
                age_to = input_valid_int('Enter age to: ')
                Employees_Manager.delete_employees_with_age()

            elif choice == '4':
                name = input('Enter employee name: ')
                salary = input_valid_int('Enter employee salary: ')
                Employees_Manager.update_salary_by_name()
            
            else:
                break
            

if __name__ == '__main__':
    app = Frontend_Manager()
    app.run()



"""
you must use the single responsibility principle
which means when u design a function it must be responsible for a single reason
The class shouldn't be a complecated class with alot of things that you are implementing together
Frontend is responsible for the interaction with the user, it reads and prints only


"""