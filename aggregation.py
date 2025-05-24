class Employee:
    def __init__(self,name):
        self.name=name


class Department:
    def __init__(self,dept_name,employee):
        self.dept_name=dept_name
        self.employee=employee
    
epm1=Employee("Asad")
print(epm1)
Dept=Department("HR",epm1)
print(Dept.dept_name,Dept.employee.name)
