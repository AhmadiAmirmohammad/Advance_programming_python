#SOLID stands for five design principles that help write cleaner,
# more maintainable,
# and more extensible code.
# It's one of the most common topics in mid-level and above interviews.

# A Class only have 1 responsibility
    #sush as 'save on database' and 'reporting'

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        return self.salary * 1.1

class EmployeeRepository:
    def save(self, employee):
        print(f" saving in database{employee.name} ")

class PayrollReportGenerator:
    def generate(self, employee):
        print(f"get reporting pdf{employee.name} ")

emp = Employee("Ali", 10_000_000)
EmployeeRepository().save(emp)
PayrollReportGenerator().generate(emp)