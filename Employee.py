# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

class Employee:
    def __init__(self, name, id, department, title):
        self.name = name
        self.id = id
        self.department = department
        self.title = title

emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
print("Name", emp1.name, "ID", emp1.id, "Department", emp1.department, "Title", emp1.title)

emp2 = Employee("Mark Jonse", 39119, "IT", "Programmer")
print("Name", emp2.name, "ID", emp2.id, "Department", emp2.department, "Title", emp2.title)

emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
print("Name", emp3.name, "ID", emp3.id, "Department", emp3.department, "Title", emp3.title)