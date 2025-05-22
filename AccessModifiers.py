class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def get_ssn(self):
        return self.__ssn

emp = Employee("Ali", "50 thousand", 3160121183)
print(emp.name)
print(emp._salary)
# print(emp.__ssn)
print(emp.get_ssn())  

